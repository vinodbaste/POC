# artifact_12

Competition: AMC
Problem ID: amc12a_2006_p11
Year: 2006

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

Find all $\theta \in [0°, 360°)$ satisfying $\sin\theta + \cos\theta = 1$.

## Candidate Excerpts

### Option A

```text
Squaring both sides: (sin θ + cos θ)^2 = 1, so
  sin²θ + 2 sin θ cos θ + cos²θ = 1
  1 + sin 2θ = 1
  sin 2θ = 0.
Thus 2θ = 0°, 180°, 360°, 540°, giving θ = 0°, 90°, 180°, 270°.
```

### Option B

```text
We must check each candidate from Step 1 in the original equation sin θ + cos θ = 1:
  θ = 0°:   sin 0° + cos 0° = 0+1 = 1 ✓
  θ = 90°:  sin 90° + cos 90° = 1+0 = 1 ✓
  θ = 180°: sin 180° + cos 180° = 0+(-1) = -1 ✗
  θ = 270°: sin 270° + cos 270° = -1+0 = -1 ✗
So the solutions are θ = 0° and θ = 90°.
```

### Option C

```text
We can write sin θ + cos θ = √2 · sin(θ + 45°). Setting this equal to 1 gives
sin(θ + 45°) = 1/√2, so θ + 45° = 45° or 135° (mod 360°), hence θ = 0° or 90°.
This confirms the solution set {0°, 90°}.
```

### Option D

```text
Since squaring can introduce extraneous solutions, the candidates θ ∈ {0°,90°,180°,270°}
must be verified in the original equation. Steps 2–3 carry out this verification,
retaining only θ = 0° and θ = 90°.
```

## Full Candidate Proof

```text
Step 1. Square both sides: sin²θ + 2 sinθ cosθ + cos²θ = 1, giving sin 2θ = 0,
so 2θ = 0°,180°,360°,540° and θ ∈ {0°,90°,180°,270°}.

Step 2. Since squaring may introduce extraneous solutions, check each candidate
in the original equation. θ=0°: 0+1=1 ✓. θ=90°: 1+0=1 ✓. θ=180°: 0-1=-1 ✗.
θ=270°: -1+0=-1 ✗. Solutions: θ=0° and θ=90°.

Step 3. Alternative: sin θ+cos θ = √2 sin(θ+45°)=1, so sin(θ+45°)=1/√2,
giving θ+45°=45° or 135°, i.e., θ=0° or 90°. Confirmed.

Step 4. Since squaring preserves solutions and Step 2 filters extraneous ones,
the final answer is {0°, 90°}.
```

## Reviewer Note

Option D (Step 4) is the first invalid step (appearing after the valid squaring and verification steps). It claims that "squaring preserves solutions," which is the opposite of the truth — squaring can introduce extraneous solutions (which is why Step 2 was necessary). The correct statement is that squaring may introduce extraneous solutions, so verification is required. The statement in Step 4 contradicts the need for the check done in Step 2 and is logically inconsistent with the rest of the proof.
