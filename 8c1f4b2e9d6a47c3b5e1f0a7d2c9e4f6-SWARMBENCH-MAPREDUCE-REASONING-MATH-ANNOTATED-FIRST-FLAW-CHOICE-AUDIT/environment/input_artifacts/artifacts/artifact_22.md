# artifact_22

Competition: IMOSL  
Problem ID: IMOSL_2020_11  
Year: 2020

Human annotation sourced from the Open Proof Corpus (INSAIT-Institute/OPC). The reviewer's free-form note identified a first logical error; four candidate proof windows have been curated from the incorrect attempt. Select the one window that spans the human-marked flaw.

## Problem

Let \( n \) be an integer with \( n \geq 2 \). On a slope of a mountain, \( n^2 \) checkpoints are marked, numbered from \( 1 \) to \( n^2 \) from the bottom to the top. Each of two cable car companies, \( A \) and \( B \), operates \( k \) cable cars numbered from \( 1 \) to \( k \); each cable car provides a transfer from some checkpoint to a higher one. For each company, and for any \( i \) and \( j \) with \( 1 \leq i < j \leq k \), the starting point of car \( j \) is higher than the starting point of car \( i \); similarly, the finishing point of car \( j \) is higher than the finishing point of car \( i \). Say that two checkpoints are linked by some company if one can start from the lower checkpoint and reach the higher one by using one or more cars of that company (no movement on foot is allowed).

Determine the smallest \( k \) for which one can guarantee that there are two checkpoints that are linked by each of the two companies.

## Candidate Excerpts

### Option A

```text
– Let \(P_A\) be the partition of \(\{1,\dots,N\}\) into the \(A\)‐connectivity blocks, say of sizes \(p\) blocks.  Since each car goes from \(a_i\) to a strictly higher \(b_i\), each interval has length \(\ge2\), so two intervals could fail to overlap only if \(k\le N/2\).  But we have \(k> N/2\), so **at least one** overlap occurs, forcing strictly fewer than \(k\) components.  Hence
\[
   \bigl|P_A\bigr|\;=\;p\;\le\;k-1.
\]
Similarly for company \(B\), the number of \(B\)‐blocks
\[
   \bigl|P_B\bigr|\;=\;q\;\le\;k-1.
\]
```

### Option B

```text
**2.1 Connectivity partitions and “cut‐points.”**  
For a family of intervals on \(\{1,2,\dots,N\}\), “linked by that company’’ means there is a chain of overlapping intervals covering from the lower checkpoint to the higher.  Equivalently, the union of the intervals splits \(\{1,\dots,N\}\) into **contiguous** connected components (blocks), each of which is an interval of integers.  We call these the *connectivity components*.
```

### Option C

```text
– Each contiguous block decomposition of \(\{1,\dots,N\}\) has “cuts’’ at the boundary points.  Concretely, a block partition has a *cut‐set*  
\[
   \partial_A \;=\;\{\,i\in\{1,\dots,N-1\}\colon\text{there is a block–boundary between $i$ and $i+1$}\},
\]
and \(|\partial_A|=p-1\).  Likewise \(|\partial_B|=q-1\).
```

### Option D

```text
---
```

## Full Candidate Proof

```text
**Solution.**  
Write \(N=n^2\).  We shall prove that the smallest \(k\) with the desired property is  
\[
   k \;=\;\Bigl\lfloor \tfrac{N}{2}\Bigr\rfloor+1
   \;=\;\Bigl\lfloor \tfrac{n^2}{2}\Bigr\rfloor+1.
\]

---

1. **A lower bound: for \(k\le \lfloor N/2\rfloor\) there is a counter‐example.**  

Set  
\[
   m \;=\;\Bigl\lfloor \tfrac{N}{2}\Bigr\rfloor
   \quad(\text{so }2m\le N<2m+2).
\]  
We define two families of \(m\) cars as follows.  Label the checkpoints \(1,2,\dots,N\).  

\medskip  
– Company \(A\): for \(i=1,2,\dots,m\) put a car from \(2i-1\) up to \(2i\).  
That is  
\[
   A_i :\;[\,2i-1,\,2i\,].
\]  
Since \(2i\!-\!1<2(i+1)\!-\!1\) and \(2i<2(i+1)\), both the start‐points and end‐points form strictly increasing sequences, as required.  

– Company \(B\): for \(i=1,2,\dots,m\) put a car from \(2i\) up to \(2i+1\).  
That is  
\[
   B_i :\;[\,2i,\,2i+1\,].
\]  
Again the starts \(2,4,6,\dots\) and ends \(3,5,7,\dots\) are strictly increasing.  (If \(N\) is even then the last car ends at checkpoint \(2m+1=N+1\), but one checks that \(2m =N\) in that case, so \(B_m\) ends at \(N\).)

\medskip  
In company \(A\), no two of the intervals \([2i-1,2i]\) overlap, so the connectivity components are exactly the \(m\) disjoint pairs  
\[
   \{1,2\},\;\{3,4\},\;\dots,\;\{2m-1,2m\}.
\]  
Similarly in \(B\) the components are the disjoint pairs  
\[
   \{2,3\},\;\{4,5\},\;\dots,\;\{2m,2m+1\}.
\]  
Any intersection of an \(A\)‐component with a \(B\)‐component is a singleton.  Hence there is **no** pair of distinct checkpoints linked by both \(A\) and \(B\).  This shows that if  
\[
   k\;\le\;\Bigl\lfloor \tfrac{N}{2}\Bigr\rfloor
\]
then one **cannot** force a common linked pair.  Thus the required \(k\) must exceed \(\lfloor N/2\rfloor\).

---

2. **An upper bound: \(\displaystyle k=\lfloor N/2\rfloor+1\) always suffices.**  

From now on set  
\[
   k \;=\;\Bigl\lfloor \tfrac{N}{2}\Bigr\rfloor+1,
\]
and let **any** two companies \(A\) and \(B\) each have \(k\) cars satisfying the stated monotonicity of start‐ and end‐points.  We show there must be two distinct checkpoints linked by both.

---

**2.1 Connectivity partitions and “cut‐points.”**  
For a family of intervals on \(\{1,2,\dots,N\}\), “linked by that company’’ means there is a chain of overlapping intervals covering from the lower checkpoint to the higher.  Equivalently, the union of the intervals splits \(\{1,\dots,N\}\) into **contiguous** connected components (blocks), each of which is an interval of integers.  We call these the *connectivity components*.  

– Let \(P_A\) be the partition of \(\{1,\dots,N\}\) into the \(A\)‐connectivity blocks, say of sizes \(p\) blocks.  Since each car goes from \(a_i\) to a strictly higher \(b_i\), each interval has length \(\ge2\), so two intervals could fail to overlap only if \(k\le N/2\).  But we have \(k> N/2\), so **at least one** overlap occurs, forcing strictly fewer than \(k\) components.  Hence
\[
   \bigl|P_A\bigr|\;=\;p\;\le\;k-1.
\]
Similarly for company \(B\), the number of \(B\)‐blocks
\[
   \bigl|P_B\bigr|\;=\;q\;\le\;k-1.
\]

– Each contiguous block decomposition of \(\{1,\dots,N\}\) has “cuts’’ at the boundary points.  Concretely, a block partition has a *cut‐set*  
\[
   \partial_A \;=\;\{\,i\in\{1,\dots,N-1\}\colon\text{there is a block–boundary between $i$ and $i+1$}\},
\]
and \(|\partial_A|=p-1\).  Likewise \(|\partial_B|=q-1\).

Now two checkpoints \(i\) and \(i+1\) lie *in the same block* of both partitions exactly if **neither** partition cuts between them, i.e.\ \(i\notin\partial_A\cup\partial_B\).  In that case \(i\) and \(i+1\) are linked by both companies, and we are done.  So it suffices to show
\[
   \partial_A\cup\partial_B \;\subsetneqq\;\{1,2,\dots,N-1\},
\]
i.e.\ that not *every* position \(1,2,\dots,N-1\) is cut by at least one of \(A,B\).

---

**2.2 Counting cuts.**  
We have
\[
   |\partial_A| \;=\; p-1 \;\le\;(k-1)-1 \;=\; k-2,
   \qquad
   |\partial_B| \;=\; q-1 \;\le\;k-2.
\]
Hence
\[
   \bigl|\partial_A\cup\partial_B\bigr|
   \;\le\;|\partial_A|+|\partial_B|
   \;\le\;2(k-2)\;=\;2k-4.
\]
But by hypothesis
\[
   k \;=\;\Bigl\lfloor \tfrac{N}{2}\Bigr\rfloor \;+\;1
   \quad\Longrightarrow\quad
   2k \;\le\; N+2,
\]
so
\[
   2k-4 \;\le\; N-2.
\]
Therefore
\[
   \bigl|\partial_A\cup\partial_B\bigr|\;\le\;N-2
   \;<\;(N-1),
\]
and so \(\partial_A\cup\partial_B\) cannot cover all \(N-1\) possible cut‐positions.  At least one integer
\[
   i\in\{1,2,\dots,N-1\}
   \quad\hbox{lies in neither }\partial_A\hbox{ nor }\partial_B.
\]
By the preceding remark, \(i\) and \(i+1\) lie in the same connectivity block *for both* companies.  Hence they are linked by \(A\) and also by \(B\).  

---

**Conclusion.**  
We have shown:

• If \(k\le\lfloor N/2\rfloor\) there is an explicit choice of two families with *no* common linked pair.  
 
• If \(k=\lfloor N/2\rfloor+1\), then *for any* two such families one finds a common linked pair.

Hence the minimal \(k\) with the required property is
\[
   k \;=\;\Bigl\lfloor \tfrac{n^2}{2}\Bigr\rfloor +1.
\]
∎
```

## Reviewer Note

Misinterprets the problem statement.
