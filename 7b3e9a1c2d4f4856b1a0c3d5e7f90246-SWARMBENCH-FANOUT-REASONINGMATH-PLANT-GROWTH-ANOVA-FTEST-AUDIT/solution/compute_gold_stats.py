#!/usr/bin/env python3
"""Deterministic gold-statistics derivation for the PlantGrowth one-way ANOVA audit.

Reads the real PlantGrowth data (environment/input_artifacts/plant_growth.csv) and
derives every quantity the audit oracle keys on with closed-form one-way ANOVA
formulae, then PRINTS them. This documents how the audit ground truth
(F(2,27) ~= 4.846) is obtained, plus the wrong-method reference values the
failure codes C1-C6 key on. It does NOT write tests/oracle.json.

Standard library only. Run from the task root:

    python3 solution/compute_gold_stats.py
"""
import csv
import math
import os

ROUND = 6


def betacf(a, b, x):
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
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(lbeta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * betacf(a, b, x) / a
    return 1.0 - front * betacf(b, a, 1.0 - x) / b


def f_sf(f, d1, d2):
    """Upper-tail p-value P(F > f) for the F(d1, d2) distribution."""
    if f <= 0:
        return 1.0
    x = d2 / (d2 + d1 * f)
    return betai(d2 / 2.0, d1 / 2.0, x)


def r(v):
    return round(float(v), ROUND)


def groups_from_csv(path):
    g = {}
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            g.setdefault(row["group"], []).append(float(row["weight"]))
    return g


def anova(groups):
    all_vals = [v for vals in groups.values() for v in vals]
    N = len(all_vals)
    k = len(groups)
    grand = sum(all_vals) / N
    ssb = sum(len(vals) * (sum(vals) / len(vals) - grand) ** 2 for vals in groups.values())
    ssw = sum((v - sum(vals) / len(vals)) ** 2 for vals in groups.values() for v in vals)
    sst = sum((v - grand) ** 2 for v in all_vals)
    df_b, df_w = k - 1, N - k
    msb, msw = ssb / df_b, ssw / df_w
    f = msb / msw
    return dict(N=N, k=k, grand=grand, ssb=ssb, ssw=ssw, sst=sst,
               df_b=df_b, df_w=df_w, msb=msb, msw=msw, f=f)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    csv_path = os.path.join(root, "environment", "input_artifacts", "plant_growth.csv")
    groups = groups_from_csv(csv_path)

    a = anova(groups)
    print("# ---- GOLD (correct one-way ANOVA on all 30 obs, 3 groups) ----")
    for name, vals in groups.items():
        print(f"  mean[{name}] = {r(sum(vals)/len(vals))}  (n={len(vals)})")
    print(f"  grand mean    = {r(a['grand'])}")
    print(f"  SSB, SSW, SST = {r(a['ssb'])}, {r(a['ssw'])}, {r(a['sst'])}")
    print(f"  df            = ({a['df_b']}, {a['df_w']})")
    print(f"  MSB, MSW      = {r(a['msb'])}, {r(a['msw'])}")
    print(f"  F             = {r(a['f'])}")
    print(f"  p-value       = {r(f_sf(a['f'], a['df_b'], a['df_w']))}")
    print(f"  >>> gold_F_x1000 = {round(a['f'] * 1000)}")

    print("\n# ---- wrong-method reference values (NOT gold) ----")
    # C1: report SSB/SSW (forgot to divide by df) as F
    print(f"  C1 ratio-of-SS F = SSB/SSW       = {r(a['ssb']/a['ssw'])}")
    # C2: wrong within df -> MSW uses N-1 instead of N-k
    msw_c2 = a['ssw'] / (a['N'] - 1)
    print(f"  C2 F with df_w=N-1=29            = {r(a['msb']/msw_c2)}")
    # C4: wrong between df -> MSB uses k instead of k-1
    msb_c4 = a['ssb'] / a['k']
    print(f"  C4 F with df_b=k=3               = {r(msb_c4/a['msw'])}")
    # C3: pairwise two-sample t (ctrl vs trt2), pooled
    g = groups
    def two_sample_t(x, y):
        nx, ny = len(x), len(y)
        mx, my = sum(x)/nx, sum(y)/ny
        sx = sum((v-mx)**2 for v in x); sy = sum((v-my)**2 for v in y)
        sp2 = (sx+sy)/(nx+ny-2)
        return (mx-my)/math.sqrt(sp2*(1/nx+1/ny))
    print(f"  C3 t(ctrl,trt2) pooled           = {r(two_sample_t(g['ctrl'], g['trt2']))}")
    print(f"  C3 t(trt1,trt2) pooled           = {r(two_sample_t(g['trt1'], g['trt2']))}")
    # C5: drop trt1 -> 2-group ANOVA on ctrl & trt2
    g2 = {"ctrl": g["ctrl"], "trt2": g["trt2"]}
    a2 = anova(g2)
    print(f"  C5 F dropping trt1 (k=2,N=20)    = {r(a2['f'])}  df=({a2['df_b']},{a2['df_w']})")


if __name__ == "__main__":
    main()
