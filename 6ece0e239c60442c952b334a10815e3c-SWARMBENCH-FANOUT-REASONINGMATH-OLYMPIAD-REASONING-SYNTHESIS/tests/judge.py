import argparse
import json
import os
import re
from openai import OpenAI

ORACLE_STATS = {
    "algebra":                  {"total": 1744, "hard": 834},
    "geometry":                 {"total": 870,  "hard": 598},
    "counting_and_probability": {"total": 771,  "hard": 442},
    "number_theory":            {"total": 869,  "hard": 500},
    "precalculus":              {"total": 746,  "hard": 352},
}
DOMAINS = list(ORACLE_STATS.keys())


def extract_json(text: str) -> str:
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
    if match:
        return match.group(1).strip()
    return text


def score_domain_statistics(agent_stats: dict) -> tuple[float, str]:
    if not agent_stats:
        return 0.0, "domain_statistics field missing."

    domain_scores, details = [], []
    for domain in DOMAINS:
        o = ORACLE_STATS[domain]
        a = agent_stats.get(domain, {})
        if not a:
            domain_scores.append(0.0)
            details.append(f"{domain}: MISSING (0.0)")
            continue

        scores = []

        # total_problems: exact
        scores.append(1.0 if a.get("total_problems") == o["total"] else 0.0)

        # hard_problems_count: ±2% of total (scales with dataset size)
        tol = max(10, int(o["total"] * 0.02))
        hard_diff = abs(a.get("hard_problems_count", 0) - o["hard"])
        scores.append(1.0 if hard_diff <= tol else (0.5 if hard_diff <= tol * 3 else 0.0))

        # level_distribution: all 5 keys present and sum matches oracle total (±1%)
        a_dist = a.get("level_distribution", {})
        lv_sum = sum(a_dist.get(f"Level {i}", 0) for i in range(1, 6))
        lv_ok = all(f"Level {i}" in a_dist for i in range(1, 6))
        tol_lv = max(10, int(o["total"] * 0.01))
        scores.append(1.0 if (lv_ok and abs(lv_sum - o["total"]) <= tol_lv) else 0.5 if lv_ok else 0.0)

        d_score = sum(scores) / len(scores)
        domain_scores.append(d_score)
        details.append(f"{domain}: {d_score:.2f} (hard={a.get('hard_problems_count',0)}/{o['hard']})")

    overall = sum(domain_scores) / len(domain_scores)
    return overall, " | ".join(details)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-output")
    parser.add_argument("--oracle")
    parser.add_argument("--reward-out")
    args = parser.parse_args()

    try:
        agent_output = json.load(open(args.agent_output))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        json.dump({"reward": 0.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write(f"Score: 0.0\n\nAgent output missing or invalid: {e}")
        return

    oracle = json.load(open(args.oracle))

    if agent_output == oracle:
        json.dump({"reward": 1.0}, open(args.reward_out, "w"))
        with open("/logs/agent/judge_justification.txt", "w") as f:
            f.write("Score: 1.0\n\nAgent output exactly matches oracle.")
        return

    # Quantitative score (35% weight)
    quant_score, quant_detail = score_domain_statistics(
        agent_output.get("domain_statistics", {})
    )

    # Qualitative score (25% weight) — 6 fields
    # Solution depth score (40% weight) — requires per-domain solution-text analysis
    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url="https://api.fireworks.ai/inference/v1",
    )

    agent_qual = {k: v for k, v in agent_output.items() if k != "domain_statistics"}
    oracle_qual = {k: v for k, v in oracle.items() if k != "domain_statistics"}

    facts = (
        "GROUND-TRUTH DOMAIN DIFFICULTY (agent analysis must be grounded in these):\n"
        "- algebra: 1744 problems, 834/1744 = 47.8% hard, largest dataset\n"
        "- precalculus: 746 problems, 352/746 = 47.2% hard, most balanced level distribution\n"
        "- counting_and_probability: 771 problems, 442/771 = 57.3% hard, Level 5 = 276/771 = 35.8%\n"
        "- number_theory: 869 problems, 500/869 = 57.5% hard, Level 5 = 313/869 = 36.0%\n"
        "- geometry: 870 problems, 598/870 = 68.7% hard — HARDEST domain, Level 5 = 421/870 = 48.4%\n"
        "Difficulty ranking (hardest first): geometry > number_theory > counting > algebra > precalculus\n"
    )

    qual_prompt = (
        "You are evaluating a mathematical reasoning synthesis task. "
        "Score 6 qualitative fields from 0.0 to 1.0.\n\n"
        + facts + "\n"
        "SCORING PRINCIPLE: The highest scores go to analysis that is DOMAIN-SPECIFIC — "
        "where each strategy, failure mode, technique, or family is clearly grounded in "
        "a particular domain's difficulty data using EXACT level-distribution fractions "
        "(e.g., '421/870=48.4%'), not just rounded percentages. Generic analysis that "
        "could describe any math dataset scores lower, even if technically correct.\n\n"
        f"ORACLE (reference):\n{json.dumps(oracle_qual, indent=2)}\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_qual, indent=2)}\n\n"
        "Score each field:\n\n"
        "Field 1 — proof_strategy_taxonomy:\n"
        "  1.0: Each strategy tied to specific domain(s) with explicit hard-% AND exact level-distribution fraction (X/Y=Z%).\n"
        "  0.7: Clear domain attribution with hard-% but missing exact level-distribution fractions.\n"
        "  0.4: Domain-agnostic strategies or valid for all 5 domains without differentiation.\n"
        "  0.0: Missing or mathematically wrong.\n\n"
        "Field 2 — reasoning_style_comparison:\n"
        "  1.0: All 5 domain keys present, each citing hard-problem rate AND exact level-distribution fractions "
        "(geometry=598/870=68.7%, number_theory=500/869=57.5%, counting=442/771=57.3%, algebra=834/1744=47.8%, precalculus=352/746=47.2%).\n"
        "  0.7: All 5 keys present with hard-% but without exact X/Y fraction form.\n"
        "  0.3: Missing domain keys or contradicts the difficulty ordering.\n"
        "  0.0: Missing or contradicts data.\n\n"
        "Field 3 — most_subtle_reasoning_failure_modes:\n"
        "  1.0: Each failure mode domain-specific, citing exact level-distribution skew (e.g., 'geometry 421/870=48.4% Level 5') "
        "AND specific solution-text patterns that cause the failure (e.g., 'solutions at Level 5 assume auxiliary constructions exist').\n"
        "  0.7: Domain-specific with hard-% but missing exact level-distribution fractions.\n"
        "  0.4: Domain-attributed but no link to difficulty data or solution patterns.\n"
        "  0.0: Generic or mathematically implausible.\n\n"
        "Field 4 — top_proof_techniques:\n"
        "  1.0: Exactly 10 techniques, each attributed to a specific domain with exact level-distribution fraction AND difficulty data.\n"
        "  0.7: 10 techniques with domain attribution and hard-% but missing exact fractions.\n"
        "  0.4: 10 techniques but generic across domains.\n"
        "  0.0: Fewer than 10 techniques or missing.\n\n"
        "Field 5 — hardest_problem_families:\n"
        "  1.0: Each family justified with exact level-distribution fraction (e.g., '421/870=48.4% Level 5') "
        "AND solution-approach pattern explaining why that fraction creates difficulty.\n"
        "  0.7: Families with hard-% but missing exact level-distribution fractions or solution patterns.\n"
        "  0.4: Generic families not grounded in computed statistics.\n"
        "  0.0: Missing or contradicts data.\n\n"
        "Field 6 — cross_domain_reasoning_transfer:\n"
        "  1.0: Synthesizes all 5 domains with exact level-distribution fractions for each, "
        "plus specific solution-technique transfer examples grounded in those fractions.\n"
        "  0.7: Good synthesis with hard-% for each domain but missing exact fractions.\n"
        "  0.4: Generic cross-domain commentary without difficulty grounding.\n"
        "  0.0: Missing or contradicts difficulty ordering.\n\n"
        "Respond in JSON only (no markdown):\n"
        '{"qualitative_score": <float 0.0-1.0>, '
        '"field_scores": {'
        '"proof_strategy_taxonomy": <f>, "reasoning_style_comparison": <f>, '
        '"most_subtle_reasoning_failure_modes": <f>, "top_proof_techniques": <f>, '
        '"hardest_problem_families": <f>, "cross_domain_reasoning_transfer": <f>}, '
        '"justification": "<field-by-field>"}'
    )

    depth_prompt = (
        "You are evaluating whether a mathematical reasoning synthesis demonstrates SYSTEMATIC "
        "per-domain solution-text analysis — evidence that the agent actually read and analyzed "
        "solution texts across all 5 domains (not just computed statistics).\n\n"
        + facts + "\n"
        "SOLUTION DEPTH CRITERIA — score 0.0 to 1.0:\n\n"
        "  1.0: For ALL 5 domains, the output provides:\n"
        "       (a) Specific solution approach patterns observed in Level 4-5 solutions "
        "(e.g., 'geometry Level 5 solutions systematically employ auxiliary circle construction as first step'),\n"
        "       (b) Evidence of technique frequency from solution text analysis (not just general math knowledge),\n"
        "       (c) Domain-specific failure patterns tied to HOW solutions are written, not just difficulty statistics.\n\n"
        "  0.7: Covers 3-4 domains with solution-text patterns; remaining domains are statistics-only.\n\n"
        "  0.4: Covers 1-2 domains with solution-text patterns; other domains are statistics or general math knowledge.\n\n"
        "  0.2: Output is primarily statistical (level counts, hard-rates) with no evidence of reading solution texts. "
        "Analysis could have been produced from just knowing domain names and difficulty levels.\n\n"
        "  0.0: No domain-specific solution patterns; entirely generic or missing.\n\n"
        "KEY DISTINCTION: Statistics (e.g., '68.7% hard-rate', '421 Level 5 problems') come from counting labels — "
        "any agent can produce these from metadata alone. Solution-text patterns require actually reading HOW problems "
        "are solved at each level. Look for evidence of the latter.\n\n"
        f"AGENT OUTPUT:\n{json.dumps(agent_qual, indent=2)}\n\n"
        "Respond in JSON only (no markdown):\n"
        '{"solution_depth_score": <float 0.0-1.0>, "justification": "<brief per-domain assessment>"}'
    )

    qual_response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p5",
        messages=[{"role": "user", "content": qual_prompt}],
        temperature=0,
    )
    depth_response = client.chat.completions.create(
        model="accounts/fireworks/models/kimi-k2p5",
        messages=[{"role": "user", "content": depth_prompt}],
        temperature=0,
    )

    raw_qual = qual_response.choices[0].message.content or ""
    try:
        result = json.loads(extract_json(raw_qual))
        # Compute qual_score directly from field_scores to avoid LLM arithmetic errors.
        field_scores = result.get("field_scores", {})
        if field_scores:
            qual_score = sum(float(v) for v in field_scores.values()) / len(field_scores)
        else:
            qual_score = float(result.get("qualitative_score", 0.0))
        qual_detail = result.get("justification", "")
    except (json.JSONDecodeError, ValueError) as e:
        qual_score = 0.0
        qual_detail = f"Parse error: {e}\nRaw: {raw_qual}"

    raw_depth = depth_response.choices[0].message.content or ""
    try:
        depth_result = json.loads(extract_json(raw_depth))
        depth_score = float(depth_result.get("solution_depth_score", 0.0))
        depth_detail = depth_result.get("justification", "")
    except (json.JSONDecodeError, ValueError) as e:
        depth_score = 0.0
        depth_detail = f"Parse error: {e}\nRaw: {raw_depth}"

    # 35% quantitative + 25% qualitative + 40% solution_depth
    final_score = round(0.35 * quant_score + 0.25 * qual_score + 0.40 * depth_score, 4)

    json.dump({"reward": final_score}, open(args.reward_out, "w"))
    with open("/logs/agent/judge_justification.txt", "w") as f:
        f.write(
            f"Score: {final_score:.4f}\n"
            f"  Quantitative  (35%): {quant_score:.4f}\n"
            f"  Qualitative   (25%): {qual_score:.4f}\n"
            f"  SolutionDepth (40%): {depth_score:.4f}\n\n"
            f"QUANTITATIVE:\n{quant_detail}\n\n"
            f"QUALITATIVE:\n{qual_detail}\n\n"
            f"SOLUTION DEPTH:\n{depth_detail}"
        )


if __name__ == "__main__":
    main()
