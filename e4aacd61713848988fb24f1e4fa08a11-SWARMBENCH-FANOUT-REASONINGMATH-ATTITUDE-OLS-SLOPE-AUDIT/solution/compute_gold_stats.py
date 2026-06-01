#!/usr/bin/env python3
"""Deterministic gold-statistics derivation for the rating-on-complaints OLS audit.

Reads the real `attitude` 2-column data (environment/input_artifacts/attitude.csv)
and derives every quantity used by the audit oracle with closed-form ordinary
least-squares formulae, then PRINTS them. This documents how the audit ground
truth (slope ~= 0.755, intercept ~= 14.376, 95% CI for the slope [0.555, 0.954],
R^2 ~= 0.681, residual SE ~= 6.993 on 28 df) is obtained. It does NOT write
tests/oracle.json (that file is the audit oracle).

No third-party packages: only the Python standard library is used. The Student-t
0.975 quantile for 28 df is obtained from the inverse regularized incomplete beta
function implemented here from scratch. Run from the task root:

    python3 solution/compute_gold_stats.py
"""
import csv
import math
import os

ROUND = 6


def _betacf(a, b, x):
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            break
    return h


def betai(a, b, x):
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def t_ppf(p, df):
    """Inverse Student-t CDF via bisection on the regularized incomplete beta."""
    if p <= 0.5:
        sign, target = -1.0, 0.5 - p
    else:
        sign, target = 1.0, p - 0.5
    lo, hi = 0.0, 1e6
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        # two-sided tail prob for t = mid: P(|T| > mid) = I_{df/(df+mid^2)}(df/2, 1/2)
        xb = df / (df + mid * mid)
        half_tail = 0.5 * betai(df / 2.0, 0.5, xb)
        cdf_minus_half = 0.5 - half_tail
        if cdf_minus_half < target:
            lo = mid
        else:
            hi = mid
    return sign * 0.5 * (lo + hi)


def r(v):
    return round(float(v), ROUND)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    csv_path = os.path.join(root, "environment", "input_artifacts", "attitude.csv")

    xs, ys = [], []
    with open(csv_path, newline="") as fh:
        for row in csv.DictReader(fh):
            xs.append(float(row["complaints"]))
            ys.append(float(row["rating"]))

    n = len(xs)
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    Sxx = sum((x - xbar) ** 2 for x in xs)
    Syy = sum((y - ybar) ** 2 for y in ys)
    Sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))

    slope = Sxy / Sxx
    intercept = ybar - slope * xbar
    sse = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    df = n - 2
    s2 = sse / df
    s = math.sqrt(s2)
    se_slope = s / math.sqrt(Sxx)
    se_intercept = s * math.sqrt(1.0 / n + xbar ** 2 / Sxx)
    r2 = 1.0 - sse / Syy
    pearson_r = Sxy / math.sqrt(Sxx * Syy)
    t_slope = slope / se_slope
    tcrit = t_ppf(0.975, df)
    ci_lo = slope - tcrit * se_slope
    ci_hi = slope + tcrit * se_slope

    # Wrong-method reference values the audit codes key on (for documentation):
    slope_reverse = Sxy / Syy                 # F1: regress complaints on rating
    sumx2 = sum(x * x for x in xs)
    sumxy = sum(x * y for x, y in zip(xs, ys))
    slope_origin = sumxy / sumx2              # F3: regression through the origin
    ci_lo_z = slope - 1.959964 * se_slope     # F4: normal 1.96 instead of t
    ci_hi_z = slope + 1.959964 * se_slope

    print(f"n               = {n}")
    print(f"xbar, ybar      = {r(xbar)}, {r(ybar)}")
    print(f"Sxx, Syy, Sxy   = {r(Sxx)}, {r(Syy)}, {r(Sxy)}")
    print(f"slope           = {r(slope)}")
    print(f"intercept       = {r(intercept)}")
    print(f"residual SE (s) = {r(s)}  on df = {df}")
    print(f"se_slope        = {r(se_slope)}")
    print(f"se_intercept    = {r(se_intercept)}")
    print(f"t_slope         = {r(t_slope)}")
    print(f"t crit (.975,df)= {r(tcrit)}")
    print(f"slope 95% CI    = [{r(ci_lo)}, {r(ci_hi)}]")
    print(f"R^2             = {r(r2)}")
    print(f"pearson r       = {r(pearson_r)}")
    print("# headline gold for the audit:")
    print(f"gold_slope_x1000 = {round(slope * 1000)}")
    print("# wrong-method reference values (NOT gold):")
    print(f"F1 reverse slope (complaints~rating) = {r(slope_reverse)}")
    print(f"F2 pearson r as slope                = {r(pearson_r)}  (R^2 = {r(r2)})")
    print(f"F3 through-origin slope               = {r(slope_origin)}")
    print(f"F4 normal-z 95% CI                    = [{r(ci_lo_z)}, {r(ci_hi_z)}]")


if __name__ == "__main__":
    main()
