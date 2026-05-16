# artifact_15

Competition: AMC
Problem ID: amc10b_2009_p15
Year: 2009

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

In triangle $ABC$, $\angle A = 90°$, $AB = 3$, and $AC = 4$. Point $D$ lies on $BC$ such that $AD \perp BC$. Find $AD$.

## Candidate Excerpts

### Option A

```text
Therefore AD = 12/5.
```

### Option B

```text
Using the area formula: Area = (1/2)·BC·AD, so 6 = (1/2)·5·AD, giving AD = 12/5.
```

### Option C

```text
By the Pythagorean theorem on triangle ABC (right-angled at A):
  BC = √(AB² + AC²) = √(9+16) = √25 = 5.
The area of triangle ABC is (1/2)·AB·AC = (1/2)·3·4 = 6.
```

### Option D

```text
Since AD is the altitude to the hypotenuse, triangles ABD and ABC are similar
(both share angle B and have a right angle). The ratio of similarity is AB/BC = 3/5.
Therefore AD/AC = AB/BC, giving AD = AC·(AB/BC) = 4·(3/5) = 12/5.
```

## Full Candidate Proof

```text
Step 1. BC = √(9+16) = 5. Area(ABC) = (1/2)·3·4 = 6.

Step 2. Since AD ⊥ BC, triangles ABD and ABC are similar (∠ADB = ∠BAC = 90°,
∠B shared). Ratio = AB/BC = 3/5, so AD/AC = 3/5, giving AD = 12/5.
[Note: the correct similarity gives AD/AB = AB/BC, not AD/AC = AB/BC.]

Step 3. From area: 6 = (1/2)·5·AD, so AD = 12/5. ✓

Step 4. AD = 12/5.
```

## Reviewer Note

Option C (Step 2) is the first invalid step. While triangles ABD and ABC are indeed similar (as stated), the proof then writes the proportion as $AD/AC = AB/BC$. This matches the sides incorrectly: in the similarity $\triangle ABD \sim \triangle ABC$, the correspondence is $A \leftrightarrow A$, $B \leftrightarrow B$, $D \leftrightarrow C$, so the correct proportion is $AD/AC = AB/BC$ only if $D$ corresponds to $C$. In fact the correct proportion from the similarity is $AD/AB = AB/BC$ (the altitude equals $AB^2/BC$), not $AD/AC$. The proof gets $AD=12/5$ by the wrong ratio that happens to give the same value as the area method (which is correct), but the similar-triangle proportion cited is wrong.
