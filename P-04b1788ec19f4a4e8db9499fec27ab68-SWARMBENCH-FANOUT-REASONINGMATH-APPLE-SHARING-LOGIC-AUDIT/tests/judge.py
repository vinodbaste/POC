#!/usr/bin/env python3
import json
import os
import re
import sys
from pathlib import Path

ANSWER_PATH = Path('/testbed/answer.json')
ORACLE_PATH = Path('/tests/oracle.json')
LOG_DIR = Path('/logs/verifier')
LOG_DIR.mkdir(parents=True, exist_ok=True)

LABELS = [
    'final_answer_correct',
    'allows_unexhausted_apples',
    'third_player_choice_model_correct',
    'tie_rule_applied_correctly',
    'turn_order_applied_correctly',
    'avoids_positive_minimum_assumption',
    'player2_exception_analysis_correct',
]
RESPONSES = list('BCDEFG')
ERROR_CODES_POINTS = 28.0

VALID_ERROR_CODES = {
    'NONE',
    'WRONG_FINAL_ANSWER',
    'FORCED_EXHAUSTION_ERROR',
    'THIRD_PLAYER_MODEL_ERROR',
    'TIE_RULE_ERROR',
    'CYCLIC_TURN_ORDER_ERROR',
    'POSITIVE_APPLE_CONSTRAINT_ERROR',
    'PLAYER2_ANALYSIS_ERROR',
    'EVEN_SPLIT_FALLACY',
    'FALSE_GOAL_VERIFICATION',
}

def normalize_tuple(s):
    if not isinstance(s, str):
        return ''
    nums = re.findall(r'-?\d+', s)
    if len(nums) != 3:
        return re.sub(r'\s+', '', s)
    return '(' + ','.join(nums[:3]) + ')'

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_reward(score, details):
    score = max(0.0, min(1.0, score))
    (LOG_DIR / 'reward.txt').write_text(f'{score:.6f}\n', encoding='utf-8')
    (LOG_DIR / 'details.json').write_text(json.dumps(details, indent=2, sort_keys=True), encoding='utf-8')
    print(f'Reward: {score:.6f}')
    print(json.dumps(details, indent=2, sort_keys=True))

try:
    expected = load_json(ORACLE_PATH)
except Exception as e:
    write_reward(0.0, {'error': f'Could not load oracle: {e}'})
    sys.exit(0)

if not ANSWER_PATH.exists():
    write_reward(0.0, {'error': 'Missing /testbed/answer.json'})
    sys.exit(0)

try:
    actual = load_json(ANSWER_PATH)
except Exception as e:
    write_reward(0.0, {'error': f'answer.json is not valid JSON: {e}'})
    sys.exit(0)

points = 0.0
max_points = 0.0
feedback = {'missing': [], 'mismatches': [], 'invalid_error_codes': [], 'awarded': {}}

# Global answer: 5 points
max_points += 5
if normalize_tuple(actual.get('derived_final_answer')) == normalize_tuple(expected['derived_final_answer']):
    points += 5
    feedback['awarded']['derived_final_answer'] = 5
else:
    feedback['mismatches'].append({
        'field': 'derived_final_answer',
        'expected': expected['derived_final_answer'],
        'actual': actual.get('derived_final_answer')
    })

responses = actual.get('responses')
if not isinstance(responses, dict):
    responses = {}
    feedback['missing'].append('responses')

for rid in RESPONSES:
    exp = expected['responses'][rid]
    got = responses.get(rid)
    if not isinstance(got, dict):
        feedback['missing'].append(f'responses.{rid}')
        # still count max points below
        got = {}
    # verdict: 2 points
    max_points += 2
    if str(got.get('verdict', '')).strip().lower() == exp['verdict']:
        points += 2
    else:
        feedback['mismatches'].append({'field': f'{rid}.verdict', 'expected': exp['verdict'], 'actual': got.get('verdict')})
    # labels: 1 point each
    got_labels = got.get('labels') if isinstance(got.get('labels'), dict) else {}
    for label in LABELS:
        max_points += 1
        if got_labels.get(label) is exp['labels'][label]:
            points += 1
        else:
            feedback['mismatches'].append({'field': f'{rid}.labels.{label}', 'expected': exp['labels'][label], 'actual': got_labels.get(label)})
    # error codes exact set: 28 points
    max_points += ERROR_CODES_POINTS
    got_codes = got.get('error_codes')
    if isinstance(got_codes, list):
        got_set = set(str(x) for x in got_codes)
        invalid = sorted(got_set - VALID_ERROR_CODES)
        if invalid:
            feedback['invalid_error_codes'].append({'response': rid, 'invalid': invalid})
    else:
        got_set = set()
    exp_set = set(exp['error_codes'])
    if got_set == exp_set:
        points += ERROR_CODES_POINTS
    else:
        feedback['mismatches'].append({'field': f'{rid}.error_codes', 'expected': sorted(exp_set), 'actual': sorted(got_set)})
    # rationale presence: 1 point
    max_points += 1
    rationale = got.get('rationale')
    if isinstance(rationale, str) and len(rationale.strip()) >= 20:
        points += 1
    else:
        feedback['mismatches'].append({'field': f'{rid}.rationale', 'expected': 'nonempty explanation at least 20 characters', 'actual': rationale})

score = points / max_points if max_points else 0.0
feedback['points'] = points
feedback['max_points'] = max_points
write_reward(score, feedback)
