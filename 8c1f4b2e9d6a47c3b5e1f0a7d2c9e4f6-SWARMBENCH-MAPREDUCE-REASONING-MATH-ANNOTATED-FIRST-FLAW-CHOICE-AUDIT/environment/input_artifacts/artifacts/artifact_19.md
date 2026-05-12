# artifact_19

Competition: IMOSL  
Problem ID: IMOSL_2022_24  
Year: 2022

Human annotation sourced from the Open Proof Corpus (INSAIT-Institute/OPC). The reviewer's free-form note identified a first logical error; four candidate proof windows have been curated from the incorrect attempt. Select the one window that spans the human-marked flaw.

## Problem

Let \( \triangle ABC \) and \( \triangle A'B'C' \) be two triangles having the same circumcircle \(\omega\), and the same orthocenter \(H\). Let \(\Omega\) be the circumcircle of the triangle determined by the lines \(AA', BB'\), and \(CC'\). Prove that \(H\), the center of \(\omega\), and the center of \(\Omega\) are collinear.

## Candidate Excerpts

### Option A

```text
Proof.  Let \(O\) be the center of the common circumcircle \(\omega\) of \(\triangle ABC\) and \(\triangle A'B'C'\), and let \(X=BB'\cap CC'\), \(Y=CC'\cap AA'\), \(Z=AA'\cap BB'\).  Let \(\Omega\) be the circle through \(X,Y,Z\), and write \(O_\Omega\) for its center.
```

### Option B

```text
1.  Power of \(H\) with respect to \(\omega\).  
Since \(\omega\) is the circumcircle of \(\triangle ABC\), the line \(AA'\) meets \(\omega\) exactly in the two points \(A\) and \(A'\).  Therefore
\[
\Pow_{\omega}(H)\;=\;HA\;\cdot\;HA'.
\]
```

### Option C

```text
We will show that \(H\) has the same power with respect to \(\omega\) and to \(\Omega\).  Once that is proved, it follows at once that \(H\) lies on the radical axis of \(\omega\) and \(\Omega\), and since the line of centers \(OO_\Omega\) is perpendicular to that radical axis, it must pass through \(H\).  Hence \(O\), \(H\), and \(O_\Omega\) are collinear.
```

### Option D

```text
2.  Power of \(H\) with respect to \(\Omega\).  
By definition \(Y=CC'\cap AA'\) and \(Z=BB'\cap AA'\), so the same line \(AA'\) meets \(\Omega\) exactly in \(Y\) and \(Z\).  Hence
\[
\Pow_{\Omega}(H)\;=\;HY\;\cdot\;HZ.
\]
```

## Full Candidate Proof

```text
Proof.  Let \(O\) be the center of the common circumcircle \(\omega\) of \(\triangle ABC\) and \(\triangle A'B'C'\), and let \(X=BB'\cap CC'\), \(Y=CC'\cap AA'\), \(Z=AA'\cap BB'\).  Let \(\Omega\) be the circle through \(X,Y,Z\), and write \(O_\Omega\) for its center.  

We will show that \(H\) has the same power with respect to \(\omega\) and to \(\Omega\).  Once that is proved, it follows at once that \(H\) lies on the radical axis of \(\omega\) and \(\Omega\), and since the line of centers \(OO_\Omega\) is perpendicular to that radical axis, it must pass through \(H\).  Hence \(O\), \(H\), and \(O_\Omega\) are collinear.

1.  Power of \(H\) with respect to \(\omega\).  
Since \(\omega\) is the circumcircle of \(\triangle ABC\), the line \(AA'\) meets \(\omega\) exactly in the two points \(A\) and \(A'\).  Therefore
\[
\Pow_{\omega}(H)\;=\;HA\;\cdot\;HA'.
\]

2.  Power of \(H\) with respect to \(\Omega\).  
By definition \(Y=CC'\cap AA'\) and \(Z=BB'\cap AA'\), so the same line \(AA'\) meets \(\Omega\) exactly in \(Y\) and \(Z\).  Hence
\[
\Pow_{\Omega}(H)\;=\;HY\;\cdot\;HZ.
\]

3.  Equality of the two products.  
It remains to show
\[
HA\;\cdot\;HA'\;=\;HY\;\cdot\;HZ.
\]
We will exhibit a similarity of triangles which forces that equality.

 (a)  In \(\triangle ABC\) the point \(H\) is the orthocenter, so 
\[
AH\;\perp\;BC.
\]
Since \(Z\) lies on \(BB'\), the directed angle 
\[
\angle ZHA
\;=\;\angle\bigl(ZH,\;HA\bigr)
\;=\;\angle\bigl(BB',\;AH\bigr)
\;=\;90^\circ\;-\;\angle\bigl(BB',\,BC\bigr).
\]
But \(B,B',C\) all lie on the same circle \(\omega\), so by the inscribed‐angle theorem
\[
\angle(BB',BC)
\;=\;\angle BAC.
\]
Hence
\[
\angle ZHA \;=\; 90^\circ - \angle BAC.
\]

 (b)  In \(\triangle A'B'C'\) likewise \(H\) is its orthocenter, so
\[
A'H\;\perp\;B'C'.
\]
Since \(Y\) lies on \(CC'\), a perfectly analogous argument gives
\[
\angle HYA'
\;=\;90^\circ\;-\;\angle\bigl(CC',\,B'C'\bigr)
\;=\;90^\circ\;-\;\angle BAC
\]
because again \(B',C',C\) lie on \(\omega\).

Thus
\[
\angle ZHA \;=\;\angle HYA'.
\]
A similar pair of computations (or by symmetry of the picture) shows also
\[
\angle ZAH \;=\;\angle HYA'.
\]
Therefore
\[
\triangle ZHA\;\sim\;\triangle HYA'
\]
by the “two angles” criterion, and consequently
\[
HA\,\cdot\,HA' \;=\; HZ\,\cdot\,HY.
\]
This is exactly the statement \(\Pow_{\omega}(H)=\Pow_{\Omega}(H)\).

4.  Conclusion.  
Since \(H\) has equal power with respect to the two circles \(\omega\) and \(\Omega\), it lies on their radical axis.  But the radical axis of two circles is perpendicular to the line of centers; hence the line \(OO_\Omega\) through the two centers meets the radical axis at \(H\).  In particular \(O\), \(H\), and \(O_\Omega\) are collinear, as claimed.  ∎
```

## Reviewer Note

Incorrect implication and calculation mistakes.
