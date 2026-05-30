#!/usr/bin/env python3
"""Derive the gold final occupied-cell count from problem.md; attach hardcoded audits."""

from __future__ import annotations

import json
import re
from pathlib import Path

PROBLEM_PATH = Path("/input_artifacts/problem.md")
OUTPUT_PATH = Path("/logs/agent/output.json")

ROWS, COLS, BAR_LEN = 18, 12, 4

# Per-response gold audits (LLM-cognitive judgment; not derivable from simulation).
GOLD_LABELS: dict[str, dict[str, object]] = {
    "A": {
        "response_id": "A",
        "final_answer_correct": False,
        "failure_reasons": [
            "wrong_bar_placement",
            "wrong_row_clear_count",
            "initial_cell_count_error",
        ],
    },
    "B": {
        "response_id": "B",
        "final_answer_correct": False,
        "failure_reasons": [
            "wrong_bar_placement",
            "wrong_row_clear_count",
        ],
    },
    "C": {
        "response_id": "C",
        "final_answer_correct": False,
        "failure_reasons": [
            "wrong_bar_placement",
            "wrong_row_clear_count",
            "invalid_or_incomplete_final_output",
        ],
    },
    "D": {
        "response_id": "D",
        "final_answer_correct": False,
        "failure_reasons": [
            "wrong_row_clear_count",
            "initial_cell_count_error",
            "correct_stacking_logic",
        ],
    },
    "E": {
        "response_id": "E",
        "final_answer_correct": False,
        "failure_reasons": [
            "initial_cell_count_error",
            "correct_stacking_logic",
        ],
    },
    "F": {
        "response_id": "F",
        "final_answer_correct": False,
        "failure_reasons": [
            "wrong_bar_placement",
            "wrong_row_clear_count",
        ],
    },
}


def parse_problem(text: str) -> tuple[set[tuple[int, int]], list[int]]:
    listing_match = re.search(r"```text[^\n]*\n(.*?)\n```", text, re.DOTALL)
    listing_block = listing_match.group(1) if listing_match else text
    cell_re = re.compile(r"\(\s*(\d+)\s*,\s*(\d+)\s*\)")
    initial_cells = {
        (int(row), int(col)) for row, col in cell_re.findall(listing_block)
    }
    bar_cols = [
        int(match)
        for match in re.findall(r"\*\s*column\s+(\d+)", text, re.IGNORECASE)
    ][:3]
    if len(bar_cols) != 3:
        raise ValueError("expected exactly three bar-drop columns in problem.md")
    return initial_cells, bar_cols


def simulate_final_occupied(initial_cells: set[tuple[int, int]], bar_cols: list[int]) -> int:
    board = set(initial_cells)
    for col in bar_cols:
        occupied_in_col = [row for row, column in board if column == col]
        bottom = (max(occupied_in_col) + 1) if occupied_in_col else 1
        for offset in range(BAR_LEN):
            board.add((bottom + offset, col))

    filled_rows = sorted(
        row
        for row in range(1, ROWS + 1)
        if all((row, column) in board for column in range(1, COLS + 1))
    )
    if filled_rows:
        shifted: set[tuple[int, int]] = set()
        for row, column in board:
            if row in filled_rows:
                continue
            drop = sum(1 for cleared in filled_rows if cleared < row)
            shifted.add((row - drop, column))
        board = shifted
    return len(board)


def main() -> None:
    problem_text = PROBLEM_PATH.read_text(encoding="utf-8")
    initial_cells, bar_cols = parse_problem(problem_text)
    gold_final = simulate_final_occupied(initial_cells, bar_cols)
    if gold_final != 141:
        raise ValueError(f"simulation produced {gold_final}, expected 141")

    output = {
        "correct_final_answer": gold_final,
        "acceptable_equivalent_answers": [str(gold_final), f"{gold_final} occupied cells"],
        "per_response_assessment": [GOLD_LABELS[letter] for letter in "ABCDEF"],
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")


if __name__ == "__main__":
    main()
