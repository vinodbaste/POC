"""Independent gold derivation for the InsectSprays one-way ANOVA F-test audit.

Pure standard library. Reproduces the gold F statistic and the signature values
behind each failure code. Run from the task root:

    python3 solution/compute_gold_stats.py
"""

import csv
import math
import os
from collections import OrderedDict

CSV = os.path.join(
    os.path.dirname(__file__),
    "..",
    "environment",
    "input_artifacts",
    "insect_sprays.csv",
)


def r(x):
    return round(x, 4)


def anova(groups):
    N = sum(len(v) for v in groups.values())
    k = len(groups)
    grand = sum(sum(v) for v in groups.values()) / N
    means = {kk: sum(v) / len(v) for kk, v in groups.items()}
    ssb = sum(len(v) * (means[kk] - grand) ** 2 for kk, v in groups.items())
    ssw = sum(sum((x - means[kk]) ** 2 for x in v) for kk, v in groups.items())
    return N, k, grand, means, ssb, ssw


def pooled_t(a, b):
    na, nb = len(a), len(b)
    ma, mb = sum(a) / na, sum(b) / nb
    sa = sum((x - ma) ** 2 for x in a)
    sb = sum((x - mb) ** 2 for x in b)
    sp2 = (sa + sb) / (na + nb - 2)
    se = math.sqrt(sp2 * (1 / na + 1 / nb))
    return ma, mb, sp2, se, (ma - mb) / se, na + nb - 2


def main():
    groups = OrderedDict()
    for row in csv.DictReader(open(CSV, newline="")):
        groups.setdefault(row["spray"], []).append(float(row["count"]))

    N, k, grand, means, ssb, ssw = anova(groups)
    dfb, dfw = k - 1, N - k
    msb, msw = ssb / dfb, ssw / dfw
    F = msb / msw
    sst = ssb + ssw

    print("# ---- GOLD (full 6-group, N=72) ----")
    print("group means:", {kk: r(means[kk]) for kk in sorted(means)})
    print(f"grand mean = {r(grand)}")
    print(f"SSB = {r(ssb)}  SSW = {r(ssw)}  SST = {r(sst)}")
    print(f"df = ({dfb}, {dfw})  MSB = {r(msb)}  MSW = {r(msw)}")
    print(f"F = {r(F)}")
    print(f"  >>> gold_F_x1000 = {round(F * 1000)}")

    print("\n# ---- wrong-method reference values (NOT gold) ----")
    print(f"  C1 sums-of-squares ratio SSB/SSW = {r(ssb / ssw)}")
    print(f"  C2 wrong within df: SSW/(N-1)={r(ssw / (N - 1))} -> F={r(msb / (ssw / (N - 1)))} on (5,71); "
          f"SSW/N={r(ssw / N)} -> F={r(msb / (ssw / N))}")
    print("  C4 F crit df=(5,66): 5% ~= 2.35, 10% ~= 1.94 (gold F clears both -> reject either way)")

    # C5: drop spray C -> 5 groups
    gI = OrderedDict((kk, v) for kk, v in groups.items() if kk != "C")
    Ni, ki, gri, mi, ssbi, sswi = anova(gI)
    print(f"  C5 drop spray C: N={Ni}, k={ki}, SSB={r(ssbi)}, SSW={r(sswi)}, df=({ki-1},{Ni-ki}), "
          f"F={r((ssbi / (ki - 1)) / (sswi / (Ni - ki)))}, SST={r(ssbi + sswi)}")

    # C3 two-sample t signatures used by J (A vs C) and L (B vs D)
    for pair in [("A", "C"), ("B", "D")]:
        ma, mb, sp2, se, t, df = pooled_t(groups[pair[0]], groups[pair[1]])
        print(f"  C3 two-sample t {pair}: m1={r(ma)} m2={r(mb)} sp2={r(sp2)} se={r(se)} t={r(t)} df={df}")


if __name__ == "__main__":
    main()
