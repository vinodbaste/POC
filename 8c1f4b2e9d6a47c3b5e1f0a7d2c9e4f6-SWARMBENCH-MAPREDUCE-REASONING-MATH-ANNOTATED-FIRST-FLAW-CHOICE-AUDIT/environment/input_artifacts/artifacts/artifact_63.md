# artifact_63

Competition: IMOSL  
Problem ID: IMOSL_2009_11  
Year: 2009

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Find the largest constant \(K\) such that for all positive reals \(a, b, c\) with \(a + b + c = 3\),
\[ a^2 + b^2 + c^2 + K \cdot abc \geq K + 3. \]

## Candidate Excerpts

### Option A

```text
Step 1.  Note a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca) = 9 - 2(ab+bc+ca).
The inequality becomes 9 - 2(ab+bc+ca) + K abc ≥ K + 3, i.e.,
   K abc - 2(ab+bc+ca) ≥ K - 6.
We seek the largest K for which this holds for all (a,b,c) with a+b+c=3 and a,b,c > 0.
```

### Option B

```text
Step 2.  At the boundary a=b=c=1, the LHS becomes K · 1 - 2 · 3 = K - 6, and the RHS is
K - 6.  Equality holds, so the constraint is tight at this point.  This is consistent with
any K, so the binding constraints come from other extreme cases.
```

### Option C

```text
Step 3.  By the standard substitution, consider the symmetric case b = c, a = 3 - 2b.
Then abc = (3-2b)·b^2 and ab+bc+ca = (3-2b)·2b + b^2 = 6b - 4b^2 + b^2 = 6b - 3b^2.
The inequality K abc - 2(ab+bc+ca) ≥ K - 6 becomes
   K(3-2b)b^2 - 2(6b - 3b^2) ≥ K - 6,
i.e., K(3b^2 - 2b^3) - 12b + 6b^2 ≥ K - 6,
i.e., K(3b^2 - 2b^3 - 1) ≥ 12b - 6b^2 - 6 = -6(1 - 2b + b^2) = -6(1-b)^2.
At b = 1: LHS = K(3 - 2 - 1) = 0, RHS = 0. ✓
For b ≠ 1, divide both sides by (1-b)^2 (positive).  We need
   K · (3b^2 - 2b^3 - 1)/(1-b)^2 ≥ -6.
Factor numerator: 3b^2 - 2b^3 - 1 = -(2b^3 - 3b^2 + 1) = -(b-1)^2(2b+1).  Hence
   K · -(b-1)^2(2b+1)/(1-b)^2 ≥ -6, i.e., -K(2b+1) ≥ -6, i.e., K(2b+1) ≤ 6.
For b in (0, 3/2), 2b+1 ∈ (1, 4), so K ≤ 6/(2b+1).  The minimum of RHS over b is achieved
as b → 3/2 (i.e., a → 0), giving K ≤ 6/4 = 3/2.
```

### Option D

```text
Step 4.  Hence K_max = 3/2.  But we should check this against the original problem:
substitute K = 3/2 and verify the inequality a^2 + b^2 + c^2 + (3/2) abc ≥ 3/2 + 3 = 9/2.
At a=b=c=1: 3 + 3/2 = 9/2. ✓ Tight.
At a=3, b=c=0 (boundary, but b,c>0): a^2+b^2+c^2 = 9, abc = 0, LHS = 9 ≥ 9/2 ✓.
So K = 3/2 works.  Combined with Step 3 showing K cannot exceed 3/2, we conclude K = 3/2.
```

## Full Candidate Proof

```text
Step 1.  Note a^2 + b^2 + c^2 = (a + b + c)^2 - 2(ab + bc + ca) = 9 - 2(ab+bc+ca).
The inequality becomes 9 - 2(ab+bc+ca) + K abc ≥ K + 3, i.e.,
   K abc - 2(ab+bc+ca) ≥ K - 6.
We seek the largest K for which this holds for all (a,b,c) with a+b+c=3 and a,b,c > 0.

Step 2.  At the boundary a=b=c=1, the LHS becomes K · 1 - 2 · 3 = K - 6, and the RHS is
K - 6.  Equality holds, so the constraint is tight at this point.  This is consistent with
any K, so the binding constraints come from other extreme cases.

Step 3.  By the standard substitution, consider the symmetric case b = c, a = 3 - 2b.
Then abc = (3-2b)·b^2 and ab+bc+ca = (3-2b)·2b + b^2 = 6b - 4b^2 + b^2 = 6b - 3b^2.
The inequality K abc - 2(ab+bc+ca) ≥ K - 6 becomes
   K(3-2b)b^2 - 2(6b - 3b^2) ≥ K - 6,
i.e., K(3b^2 - 2b^3) - 12b + 6b^2 ≥ K - 6,
i.e., K(3b^2 - 2b^3 - 1) ≥ 12b - 6b^2 - 6 = -6(1 - 2b + b^2) = -6(1-b)^2.
At b = 1: LHS = K(3 - 2 - 1) = 0, RHS = 0. ✓
For b ≠ 1, divide both sides by (1-b)^2 (positive).  We need
   K · (3b^2 - 2b^3 - 1)/(1-b)^2 ≥ -6.
Factor numerator: 3b^2 - 2b^3 - 1 = -(2b^3 - 3b^2 + 1) = -(b-1)^2(2b+1).  Hence
   K · -(b-1)^2(2b+1)/(1-b)^2 ≥ -6, i.e., -K(2b+1) ≥ -6, i.e., K(2b+1) ≤ 6.
For b in (0, 3/2), 2b+1 ∈ (1, 4), so K ≤ 6/(2b+1).  The minimum of RHS over b is achieved
as b → 3/2 (i.e., a → 0), giving K ≤ 6/4 = 3/2.

Step 4.  Hence K_max = 3/2.  But we should check this against the original problem:
substitute K = 3/2 and verify the inequality a^2 + b^2 + c^2 + (3/2) abc ≥ 3/2 + 3 = 9/2.
At a=b=c=1: 3 + 3/2 = 9/2. ✓ Tight.
At a=3, b=c=0 (boundary, but b,c>0): a^2+b^2+c^2 = 9, abc = 0, LHS = 9 ≥ 9/2 ✓.
So K = 3/2 works.  Combined with Step 3 showing K cannot exceed 3/2, we conclude K = 3/2.
```

## Reviewer Note

In Step 1, "We seek the largest K for which this holds for all (a,b,c) with a+b+c=3 and a,b,c > 0" — the proof states this as the problem reformulation, but it has not yet shown that K abc - 2(ab+bc+ca) ≥ K - 6 is the correct rearrangement of the original inequality for all relevant cases. The original inequality is a^2 + b^2 + c^2 + K abc ≥ K + 3, which rearranged gives K abc - K ≥ 3 - (a^2+b^2+c^2) = 3 - (9 - 2(ab+bc+ca)) = -6 + 2(ab+bc+ca), so K(abc - 1) ≥ 2(ab+bc+ca) - 6. The proof's rearrangement instead writes K abc - 2(ab+bc+ca) ≥ K - 6, which is K abc - K ≥ 2(ab+bc+ca) - 6, i.e., K(abc - 1) ≥ 2(ab+bc+ca) - 6 — actually this matches.  But the move from "≥ 0 conclusion" to "largest K" is asserted without addressing the cases where abc - 1 changes sign: the direction of the inequality reverses when abc < 1, which is not addressed.
