# artifact_27

Competition: USAMO  
Problem ID: USAMO_2016_3  
Year: 2016

Benchmark curation item — source: INSAIT-Institute/OPC. The original human annotation flagged one step as the first unrecoverable error in this proof attempt. Four candidate excerpts (labeled A–D in shuffled order) have been extracted from that proof. Identify the excerpt containing that step.

## Problem

Let $A B C$ be an acute triangle and let $I_{B}, I_{C}$, and $O$ denote its $B$-excenter, $C$ excenter, and circumcenter, respectively. Points $E$ and $Y$ are selected on $\overline{A C}$ such that $\angle A B Y=\angle C B Y$ and $\overline{B E} \perp \overline{A C}$. Similarly, points $F$ and $Z$ are selected on $\overline{A B}$ such that $\angle A C Z=\angle B C Z$ and $\overline{C F} \perp \overline{A B}$.

Lines $I_{B} F$ and $I_{C} E$ meet at $P$. Prove that $\overline{P O}$ and $\overline{Y Z}$ are perpendicular.

## Candidate Excerpts

### Option A

```text
Indeed:
    –  Since \(F\) lies on \(\omega\), its power to \(\omega\) is zero: 
       \(\operatorname{Pow}_{\omega}(F)=0\).  
       On the other hand \(F\) also lies on the circle of radius \(I_BF\) about \(I_B\), namely \(\Gamma_B\).  Hence 
       \(\operatorname{Pow}_{\Gamma_B}(F)=F I_B^2 -(\text{radius of }\Gamma_B)^2 =0.\)  
       Thus \(F\) has equal power w.r.t. \(\omega\) and \(\Gamma_B\), so \(F\) lies on their radical axis.  Since \(I_B\) clearly lies on the radical axis of \(\omega\) and its own excircle, the line \(I_BF\) is that radical axis.
```

### Option B

```text
–  Similarly \(E\in\omega\cap\Gamma_C\), so by the same argument \(I_CE\) is the radical axis of \(\omega\) and \(\Gamma_C\).
```

### Option C

```text
2.  Let \(\Gamma_B\) be the \(B\)-excircle of \(\triangle ABC\), with center \(I_B\), and let \(\Gamma_C\) be the \(C\)-excircle, with center \(I_C\).
```

### Option D

```text
3.  We claim that
    •  the line \(I_BF\) is the radical axis of \(\omega\) and \(\Gamma_B\), and
    •  the line \(I_CE\) is the radical axis of \(\omega\) and \(\Gamma_C\).
```

## Full Candidate Proof

```text
Proof.

We begin by introducing three circles and identifying several of their common chords.

1.  Let ω be the circle with diameter BC.  Since  
    \[
      \angle BEC \;=\;\angle (BE,EC)
        \;=\;(90^\circ,\text{ line }AC)
        \;=\;90^\circ,
    \]
    the point \(E\) lies on the circle with diameter \(BC\).  Likewise
    \[
      \angle BFC
        \;=\;
      \angle (CF,FB)
        \;=\;
      (90^\circ,\text{ line }AB)
        \;=\;90^\circ,
    \]
    so \(F\) also lies on the circle with diameter \(BC\).  Hence
    \(E,F\in\omega\).

2.  Let \(\Gamma_B\) be the \(B\)-excircle of \(\triangle ABC\), with center \(I_B\), and let \(\Gamma_C\) be the \(C\)-excircle, with center \(I_C\).

3.  We claim that
    •  the line \(I_BF\) is the radical axis of \(\omega\) and \(\Gamma_B\), and
    •  the line \(I_CE\) is the radical axis of \(\omega\) and \(\Gamma_C\).

    Indeed:
    –  Since \(F\) lies on \(\omega\), its power to \(\omega\) is zero: 
       \(\operatorname{Pow}_{\omega}(F)=0\).  
       On the other hand \(F\) also lies on the circle of radius \(I_BF\) about \(I_B\), namely \(\Gamma_B\).  Hence 
       \(\operatorname{Pow}_{\Gamma_B}(F)=F I_B^2 -(\text{radius of }\Gamma_B)^2 =0.\)  
       Thus \(F\) has equal power w.r.t. \(\omega\) and \(\Gamma_B\), so \(F\) lies on their radical axis.  Since \(I_B\) clearly lies on the radical axis of \(\omega\) and its own excircle, the line \(I_BF\) is that radical axis.

    –  Similarly \(E\in\omega\cap\Gamma_C\), so by the same argument \(I_CE\) is the radical axis of \(\omega\) and \(\Gamma_C\).

4.  Let
    \[
      P \;=\;(I_BF)\;\cap\;(I_CE).
    \]
    Then \(P\) lies on both of the above radical axes.  Hence \(P\) has equal power to each of the three circles \(\omega,\Gamma_B,\Gamma_C\).  It follows that
    \[
      P
      \;\in\;
      \text{Radical axis of }\Gamma_B\text{ and }\Gamma_C.
    \]
    We denote that common radical axis by \(\ell\).

5.  We now show that the line \(\ell\) is exactly the line \(YZ\). 

    Claim.  The internal angle‐bisector of \(\angle ABC\) meets \(AC\) at \(Y\), and likewise the internal bisector of \(\angle ACB\) meets \(AB\) at \(Z\).  Each of these two bisector‐lines is the radical axis of the two excircles not centered at that vertex.  In particular, their intersection \(Y\!Z\) is the radical axis of \(\Gamma_B\) and \(\Gamma_C\).

    Proof of Claim (sketch).  A well‐known property of excircles is that the internal bisector at \(B\) is the locus of points having equal power to the \(B\)- and \(C\)-excircles.  Equivalently, any point on the internal bisector from \(B\) sees the two excircles under equal tangents.  Hence that bisector is the radical axis of \(\Gamma_B\) and \(\Gamma_C\).  Since \(Y\) lies on the bisector at \(B\) and \(Z\) on the bisector at \(C\), the line \(YZ\) is their common radical axis.  ▢

6.  From steps 4–5 we conclude
    \[
      P\in\ell
      \quad\text{and}\quad
      \ell = YZ.
    \]
    Therefore
    \[
      P\in YZ.
    \]

7.  Finally, recall the basic “radical‐axis‐perpendicularity” theorem:

    The radical axis of two circles is perpendicular to the line joining their centers.

    Applying this to the two excircles \(\Gamma_B\) and \(\Gamma_C\), whose centers are \(I_B\) and \(I_C\), we get
    \[
      I_BI_C
      \;\perp\;
      \text{Radical axis of }\Gamma_B,\Gamma_C
      \;=\;YZ.
    \]
    But we also noted in step 4 that \(P\) lies on the radical axis of \(\Gamma_B,\Gamma_C\).  Hence the line through \(P\) parallel to \(I_BI_C\) must also be perpendicular to \(YZ\).

    It remains only to observe that \(O\), the circumcenter of \(\triangle ABC\), is collinear with \(I_B\) and \(I_C\).  Indeed, in the excentral triangle \(I_B I_C I_A\) the circumcenter of \(\triangle ABC\) is the nine-point center, which lies on the line \(I_BI_C\).  Equivalently one checks by directed‐angle chasing that \(O\) lies on the perpendicular bisector of \(BC\), and the excenters \(I_B,I_C\) also lie symmetrically with respect to that same perpendicular bisector; hence \(O,I_B,I_C\) are collinear.

8.  Putting these facts together,

    –  \(P\) lies on the radical axis of \(\Gamma_B,\Gamma_C\), namely on \(YZ\);

    –  \(O\) lies on the line of centers \(I_BI_C\);

    –  the radical axis \(YZ\) is perpendicular to \(I_BI_C\).

    Therefore the line \(PO\) (which lies in the same direction as \(I_BI_C\)) is perpendicular to \(YZ\), as claimed.

This completes the proof that
\[
  PO\;\perp\;YZ.
\]
∎
```

## Reviewer Note

Incorrect radical axis statement
