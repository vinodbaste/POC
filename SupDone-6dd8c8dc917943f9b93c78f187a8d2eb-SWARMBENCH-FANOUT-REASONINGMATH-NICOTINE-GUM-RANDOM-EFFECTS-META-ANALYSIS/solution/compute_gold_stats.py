#!/usr/bin/env python3
"""Deterministic gold-statistics derivation for the nicotine-gum meta-analysis.

Reads the real 2x2 trial data (environment/input_artifacts/trials.csv) and derives
every per-study and corpus-level statistic with closed-form formulae, then PRINTS
them. This documents how the audit ground truth (random-effects pooled OR = 1.75,
95% CI [1.48, 2.07], fixed-effect OR = 1.65, I^2 = 28.3%, tau^2 = 0.047) is
obtained. It does NOT write tests/oracle.json (that file is the audit oracle).

No third-party packages: only the Python standard library is used. Run from the
task root:

    python3 solution/compute_gold_stats.py
"""
import csv
import json
import math
import os

ROUND = 6


def phi(x):
    """Standard normal CDF via erf."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def two_sided_p(z):
    return 2.0 * (1.0 - phi(abs(z)))


def chisq_sf(x, k):
    """Upper-tail probability P(X > x) for a chi-square with k dof.

    Uses the regularized upper incomplete gamma Q(a, t) with a = k/2, t = x/2
    via the standard series (lower) / continued-fraction (upper) split.
    """
    if x <= 0:
        return 1.0
    a = k / 2.0
    t = x / 2.0
    return _gammaincc(a, t)


def _gammaincc(a, x):
    if x < a + 1.0:
        return 1.0 - _gser(a, x)
    return _gcf(a, x)


def _gser(a, x):
    gln = math.lgamma(a)
    ap = a
    summ = 1.0 / a
    delta = summ
    for _ in range(1000):
        ap += 1.0
        delta *= x / ap
        summ += delta
        if abs(delta) < abs(summ) * 1e-15:
            break
    return summ * math.exp(-x + a * math.log(x) - gln)


def _gcf(a, x):
    gln = math.lgamma(a)
    tiny = 1e-300
    b = x + 1.0 - a
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, 1000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delt = d * c
        h *= delt
        if abs(delt - 1.0) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - gln) * h


def r(v):
    return round(float(v), ROUND)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    csv_path = os.path.join(root, "environment", "input_artifacts", "trials.csv")

    studies = []
    with open(csv_path, newline="") as fh:
        for row in csv.DictReader(fh):
            qt, tt, qc, tc = (int(row[k]) for k in ("qt", "tt", "qc", "tc"))
            a = qt            # treated quitters
            b = tt - qt       # treated non-quitters
            c = qc            # control quitters
            d = tc - qc       # control non-quitters
            log_or = math.log((a * d) / (b * c))
            var = 1.0 / a + 1.0 / b + 1.0 / c + 1.0 / d
            se = math.sqrt(var)
            w = 1.0 / var
            z = log_or / se
            p = two_sided_p(z)
            studies.append({
                "id": row["study"],
                "log_or": log_or, "var": var, "se": se, "w": w,
                "or": math.exp(log_or), "z": z, "p": p,
            })

    # Fixed-effect (inverse-variance) pooling.
    sum_w = sum(s["w"] for s in studies)
    sum_wy = sum(s["w"] * s["log_or"] for s in studies)
    fe_log = sum_wy / sum_w
    fe_se = math.sqrt(1.0 / sum_w)
    fe_z = fe_log / fe_se
    fe_p = two_sided_p(fe_z)

    # Heterogeneity.
    k = len(studies)
    df = k - 1
    Q = sum(s["w"] * (s["log_or"] - fe_log) ** 2 for s in studies)
    Q_p = chisq_sf(Q, df)
    sum_w2 = sum(s["w"] ** 2 for s in studies)
    C = sum_w - sum_w2 / sum_w
    tau2 = max(0.0, (Q - df) / C)
    I2 = max(0.0, (Q - df) / Q) * 100.0

    # Random-effects (DerSimonian-Laird) pooling.
    re_w = [1.0 / (s["var"] + tau2) for s in studies]
    sum_rw = sum(re_w)
    sum_rwy = sum(rw * s["log_or"] for rw, s in zip(re_w, studies))
    re_log = sum_rwy / sum_rw
    re_se = math.sqrt(1.0 / sum_rw)
    re_z = re_log / re_se
    re_p = two_sided_p(re_z)

    per_study = {}
    for s in studies:
        per_study[s["id"]] = {
            "log_odds_ratio": r(s["log_or"]),
            "variance": r(s["var"]),
            "std_error": r(s["se"]),
            "weight_fixed": r(s["w"]),
            "odds_ratio": r(s["or"]),
            "z_value": r(s["z"]),
            "p_value": r(s["p"]),
            "significant_05": bool(s["p"] < 0.05),
        }

    n_sig = sum(1 for s in studies if s["p"] < 0.05)
    study_max_w = max(studies, key=lambda s: s["w"])["id"]
    study_max_or = max(studies, key=lambda s: s["or"])["id"]
    study_min_or = min(studies, key=lambda s: s["or"])["id"]

    oracle = {
        "per_study": per_study,
        "fixed_effect": {
            "pooled_log_odds_ratio": r(fe_log),
            "std_error": r(fe_se),
            "pooled_odds_ratio": r(math.exp(fe_log)),
            "ci_lower_or": r(math.exp(fe_log - 1.96 * fe_se)),
            "ci_upper_or": r(math.exp(fe_log + 1.96 * fe_se)),
            "z_value": r(fe_z),
            "p_value": r(fe_p),
        },
        "heterogeneity": {
            "Q": r(Q),
            "df": df,
            "p_value": r(Q_p),
            "I_squared": r(I2),
            "tau_squared": r(tau2),
        },
        "random_effects": {
            "pooled_log_odds_ratio": r(re_log),
            "std_error": r(re_se),
            "pooled_odds_ratio": r(math.exp(re_log)),
            "ci_lower_or": r(math.exp(re_log - 1.96 * re_se)),
            "ci_upper_or": r(math.exp(re_log + 1.96 * re_se)),
            "z_value": r(re_z),
            "p_value": r(re_p),
        },
        "summary": {
            "n_studies": k,
            "n_significant_05": n_sig,
            "study_max_weight_fixed": study_max_w,
            "study_max_odds_ratio": study_max_or,
            "study_min_odds_ratio": study_min_or,
        },
    }

    # This is documentation-only tooling: it derives and PRINTS the gold
    # statistics that ground the audit oracle (random-effects OR = 1.75, etc.).
    # It deliberately does NOT write oracle.json, which is the audit oracle.
    print(json.dumps(oracle, indent=2, sort_keys=True))
    print("\n# headline gold for the audit:")
    print("random_effects_pooled_or =", oracle["random_effects"]["pooled_odds_ratio"])
    print("random_effects_ci        =", [oracle["random_effects"]["ci_lower_or"],
                                         oracle["random_effects"]["ci_upper_or"]])
    print("fixed_effect_pooled_or   =", oracle["fixed_effect"]["pooled_odds_ratio"])
    print("I_squared, tau_squared   =", oracle["heterogeneity"]["I_squared"],
          oracle["heterogeneity"]["tau_squared"])


if __name__ == "__main__":
    main()
