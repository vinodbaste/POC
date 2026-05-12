# Oracle Derivation — First-Step-Error Choice Audit

Source: Qwen/ProcessBench (https://huggingface.co/datasets/Qwen/ProcessBench)
Split: olympiadbench (28 artifacts)

## Step Index Convention

ProcessBench stores solutions as zero-indexed arrays: `steps[0]` is Step 1, `steps[1]` is Step 2, etc.
The `label` field is a zero-based integer: `label=L` means `steps[L]` is the first erroneous step.

## How Each Option Letter Was Assigned

For each artifact the erroneous step (`steps[label]`) was assigned to the oracle option letter shown below.
Three distractor steps were chosen from positions spread across the solution (approx. 1/4, 2/4, 3/4 of the remaining steps), then the four steps were shuffled into options A–D.

To verify artifact_NN → Option X: open `environment/input_artifacts/artifacts/artifact_NN.md`,
find `### Option X`, and confirm its text matches `steps[label]` from the ProcessBench row.

## Per-Artifact Derivation

| Artifact | Source | label (0-idx) | Step position | Option | Error step text (first 120 chars) |
|---|---|---|---|---|---|
| artifact_01 | OLYMPIADBENCH_338 | 15 | step 16/27 | **A** | Third, if \( k = 3 \), then \( 3 + (n-1) \cdot 9 = 306 \) gives \( n = 35 \). |
| artifact_02 | OLYMPIADBENCH_244 | 13 | step 14/20 | **A** | First, for \((m, k) = (1, 1)\): \[ z = \frac{-1 + 1}{4} = 0 \quad \text{and} \quad z = \frac{-1 - 1}{4} |
| artifact_03 | OLYMPIADBENCH_110 | 10 | step 11/19 | **B** | Now, we need to find distinct digits \(\mathrm{D}, \mathrm{S}, \mathrm{E}, \mathrm{H}\) that satisfy this eq |
| artifact_04 | OLYMPIADBENCH_120 | 7 | step 8/19 | **C** | For \( x^2 \) to be non-negative, \( k(10 - k) \geq 0 \). This inequality holds when \( 0 < k \leq 10 \). |
| artifact_05 | OLYMPIADBENCH_221 | 6 | step 7/18 | **D** | Sixth, for a polynomial of degree \( n \), there are \( \lfloor \frac{n+1}{2} \rfloor \) unique coefficients |
| artifact_06 | OLYMPIADBENCH_239 | 6 | step 7/17 | **D** | Simplify the right-hand side: \[ \frac{6^b}{3^b} = \left(\frac{6}{3}\right)^b = 3^b \] |
| artifact_07 | OLYMPIADBENCH_13 | 9 | step 10/16 | **A** | Using the change of base formula, we know: \[ \log_2 3 = \frac{1}{\log_3 2} \] Substitute \( \log_2 3 = \frac |
| artifact_08 | OLYMPIADBENCH_138 | 7 | step 8/16 | **C** | However, \(y-3 \geq 0\) since \(y = \log_2 x > 0\) when \(x > 1\), so we only need to consider the positive |
| artifact_09 | OLYMPIADBENCH_214 | 7 | step 8/16 | **B** | Now, substitute \(x^2\) from this expression into equation (1a): \[ (1000y^3) \cdot y^2 = 10^{11} \] |
| artifact_10 | OLYMPIADBENCH_108 | 7 | step 8/15 | **C** | The volume of \(\mathcal{C}_k\) is: \[ V_k = a_k^3 = \left(5 (\sqrt{3})^{k-1}\right)^3 = 125 \cdot 3^{k-1} \] |
| artifact_11 | OLYMPIADBENCH_76 | 7 | step 8/14 | **D** | Similarly, if \( b > 9 \) or \( c > 9 \), the same calculation applies: \[ \binom{14 + 2}{2} = 120 \] |
| artifact_12 | OLYMPIADBENCH_188 | 8 | step 9/14 | **A** | But now, we have \( a = 0.2569 \), which does not satisfy the condition \( 1 \leq a < 10 \). So, we should ke |
| artifact_13 | OLYMPIADBENCH_249 | 8 | step 9/14 | **C** | To simplify, notice that both terms have a similar structure. Let's find a common denominator: |
| artifact_14 | OLYMPIADBENCH_256 | 6 | step 7/14 | **A** | To check if \( f \) is injective, assume \( f(a) = f(b) \). We need to show that \( a = b \). Substitute |
| artifact_15 | OLYMPIADBENCH_199 | 6 | step 7/13 | **B** | ### Verification of \((57 - 8\sqrt{5}i)(-6 + 5\sqrt{5}i)\): \[ (57 - 8\sqrt{5}i)(-6 + 5\sqrt{5}i) = \] |
| artifact_16 | OLYMPIADBENCH_80 | 7 | step 8/12 | **D** | Calculating the left side gives us: \[ 0.971 \times 1.164231 \approx 1.1358 \] |
| artifact_17 | OLYMPIADBENCH_91 | 6 | step 7/12 | **C** | Simplify and solve for \( C \): \[ 6C - 4 = 10C - 20n \] \[ 6C - 10C = -20n - 4 \] \[ 4C = 20n + 4 \] |
| artifact_18 | OLYMPIADBENCH_71 | 6 | step 7/11 | **D** | We need \( 4n - 2k + 1 = 10 \) or \( 4n - 2k - 2 = 10 \) for the coefficients of \( x^{10} \). |
| artifact_19 | OLYMPIADBENCH_97 | 6 | step 7/11 | **A** | We need to find the smallest positive integer \( n \) such that \( n^4 \equiv 1 \pmod{13} \). This means \( n |
| artifact_20 | OLYMPIADBENCH_107 | 7 | step 8/11 | **C** | Since \( r = 10^{T-1} \bmod 33 \) and \( 10^{T-1} \) is a multiple of 11 for \( T \geq 3 \), \( r \) is a m |
| artifact_21 | OLYMPIADBENCH_117 | 7 | step 8/11 | **B** | Analyzing Sum and Product Constraints: Given the constraints on \(a\) and \(b\), we need to consider their su |
| artifact_22 | OLYMPIADBENCH_88 | 6 | step 7/10 | **A** | Given that \( f(1) = \frac{k}{2(k-1)} \), we need \( k = 2l + 1 \) for some \( l \in \mathbb{N} \) to ensure |
| artifact_23 | OLYMPIADBENCH_111 | 6 | step 7/10 | **D** | Now substitute \( a \) and \( d \) into the sum equation: \[ \frac{n}{2} \left(2 \left(5 - \frac{180}{n-5}\r |
| artifact_24 | OLYMPIADBENCH_180 | 5 | step 6/10 | **B** | Find the measure of \( \angle ARM \): Since \( \angle RAP = 6^\circ \), we have: \[ \angle RAM = 6^\circ \] |
| artifact_25 | OLYMPIADBENCH_317 | 5 | step 6/10 | **C** | First, consider the subcase where \(b = 2\). If \(b = 2\), then the equations become: \[ 4 - c = 2^x, \] |
| artifact_26 | OLYMPIADBENCH_21 | 5 | step 6/9 | **A** | Second, if \(b = 2\), then \(a = 60\) and \(\frac{2(2) + 1}{2^2 + 2} = \frac{5}{6}\). |
| artifact_27 | OLYMPIADBENCH_55 | 4 | step 5/9 | **D** | Fifth, approximate \( y^{34} \). Since \( 0 < y < 1 \), \( y^{34} \) is extremely small. We need to estimate |
| artifact_28 | OLYMPIADBENCH_220 | 5 | step 6/9 | **C** | If \( \alpha = 1 \), then substituting \( \alpha = 1 \) into equation (1) gives: \[ 1 + b + c = 0 \implies b |

## Option Balance

Global: A=8, B=5, C=8, D=7

Shard breakdown (natural annotation pattern — shards 1, 2, 5, 6, 7 are unbalanced):
- shard_01 (artifact_01–04): A=2, B=1, C=1, D=0
- shard_02 (artifact_05–08): A=1, B=0, C=1, D=2
- shard_03 (artifact_09–12): A=1, B=1, C=1, D=1
- shard_04 (artifact_13–16): A=1, B=1, C=1, D=1
- shard_05 (artifact_17–20): A=1, B=0, C=2, D=1
- shard_06 (artifact_21–24): A=1, B=2, C=0, D=1
- shard_07 (artifact_25–28): A=1, B=0, C=2, D=1

## Selection Criteria

- label ≥ 4 AND steps ≥ 8 (error deep in a long solution)
- depth = label/steps ≥ 0.50 (error in second half)
- Reviewer notes contain the specific mathematical error identified from reading `steps[label]`
- Distractors spread across the solution so no positional pattern exists
