# artifact_36

Competition: IMOSL  
Problem ID: IMOSL_2016_5  
Year: 2016

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Prove that for all real numbers \(a, b\):
\[
a^2 + b^2 \;\ge\; 2ab.
\]

## Candidate Excerpts

### Option A

```text
Introduce the substitution \(u = a - b\) and \(v = a + b\), so that \(a = (u+v)/2\)
and \(b = (v-u)/2\).  We will work in terms of \(u\) and \(v\).
```

### Option B

```text
Compute:
\[
a^2 + b^2 - 2ab
= \left(\frac{u+v}{2}\right)^2 + \left(\frac{v-u}{2}\right)^2 - 2\cdot\frac{u+v}{2}\cdot\frac{v-u}{2}.
\]
Expanding:
\[
= \frac{(u+v)^2 + (v-u)^2 - 2(v+u)(v-u)}{4}
= \frac{2u^2 + 2v^2 - 2(v^2 - u^2)}{4}
= \frac{4u^2}{4} = u^2.
\]
```

### Option C

```text
Since \(u = a - b\) is a real number, \(u^2 \ge 0\).  Therefore
\(a^2 + b^2 - 2ab = u^2 \ge 0\), giving \(a^2 + b^2 \ge 2ab\).  \(\square\)
```

### Option D

```text
Equality holds when \(u^2 = 0\), i.e.\ \(u = 0\), i.e.\ \(a = b\).  To confirm the
substitution is invertible: \(a = (u+v)/2\) and \(b = (v-u)/2\) with free parameter \(v\),
so equality holds for the entire family \(a = b = v/2\) for any \(v \in \mathbb{R}\).
Since \(v\) is arbitrary, equality actually holds for all \(a = b\) — but also when
\(v = 0\), giving \(a = u/2\) and \(b = -u/2 = -a\), i.e.\ \(a + b = 0\).
Therefore equality holds iff \(a = b\) OR \(a + b = 0\).
```

## Full Candidate Proof

```text
Substitution: u=a−b, v=a+b.  a²+b²−2ab = u² ≥ 0. ✓

Equality holds when u²=0, i.e., u=0, i.e., a=b.  To confirm the
substitution is invertible: a=(u+v)/2 and b=(v−u)/2 with free parameter v,
so equality holds for the entire family a=b=v/2 for any v∈ℝ.
Since v is arbitrary, equality actually holds for all a=b — but also when
v=0, giving a=u/2 and b=−u/2=−a, i.e., a+b=0.
Therefore equality holds iff a=b OR a+b=0.
```

## Reviewer Note

After correctly identifying \(a=b\) as the equality condition, the conclusion step introduces a spurious second equality case \(a+b=0\) by misreading the invertibility of the substitution.
