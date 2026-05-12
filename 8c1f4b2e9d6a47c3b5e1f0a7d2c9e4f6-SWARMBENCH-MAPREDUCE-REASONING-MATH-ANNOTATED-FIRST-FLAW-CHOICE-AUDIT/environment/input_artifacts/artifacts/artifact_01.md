# artifact_01

Competition: BMOSL  
Problem ID: BMOSL_2018_15  
Year: 2018

You are reviewing a real human annotation from the Open Proof Corpus. A curator converted one free-form annotation into four candidate proof excerpts. Exactly one candidate excerpt contains the human-marked first unrecoverable flaw in this incorrect proof attempt. Choose the correct option letter. The candidate excerpts are presented in a randomized order.

## Problem

In a triangle \(ABC\) with \(AB = AC\), \(\omega\) is the circumcircle and \(O\) its center. Let \(D\) be a point on the extension of \(BA\) beyond \(A\). The circumcircle \(\omega_1\) of triangle \(OAD\) intersects the line \(AC\) and the circle \(\omega\) again at points \(E\) and \(G\), respectively. Point \(H\) is such that \(DAEH\) is a parallelogram. Line \(EH\) meets circle \(\omega_1\) again at point \(J\). The line through \(G\) perpendicular to \(GB\) meets \(\omega_1\) again at point \(N\) and the line through \(G\) perpendicular to \(GJ\) meets \(\omega\) again at point \(L\). Prove that the points \(L, N, H, G\) lie on a circle.

## Candidate Excerpts

### Option A

```text
4.  Computation of $\angle LHN$.  
We next show that
  $$\angle LHN=\angle GBA$$
as well.  We do this by expressing $\angle LHN$ in terms of the two angles in (2), (3).
```

### Option B

```text
2.  Two angle‐equalities on $\omega_{1}$.  
On the circle $\omega_{1}$ the points $A,D,E,G,J,N,O$ are concyclic.  Hence
  (i)  {\it inscribed angles on the same arc $AG$ are equal:}
      $$\angle ADG \;=\;\angle AEG\,. $$
  But $AE\parallel DH$, so
      $$\angle AEG \;=\;\angle DHG\,. $$
  Altogether,
      $$\boxed{\;\angle ADG=\angle DHG\,.}\tag{2}$$
```

### Option C

```text
(ii)  Also on $\omega_{1}$, angles subtending the same arc $DG$ satisfy
      $$\angle DNG \;=\;\angle DEG\,. $$
  And $DE\parallel AH$, so
      $$\angle DEG \;=\;\angle AHG\,. $$
  Hence
      $$\boxed{\;\angle DNG=\angle AHG\,.}\tag{3}$$
```

### Option D

```text
3.  Computation of $\angle LGN$.  
By definition, $L$ is the second intersection of $\omega$ with the line through $G$ perpendicular to $GJ$.  Thus
  $$GL\;\perp\;GJ.$$
Similarly $N$ is the second intersection of $\omega_{1}$ with the line through $G$ perpendicular to $GB$, so
  $$GN\;\perp\;GB.$$
But $GJ\parallel DA$ by (1):  since $EH\parallel DA$ and $J\in EH$, we have $GJ\parallel DA$, and $DA$ coincides with the extension of $BA$.  Therefore
  $$\angle LGN
    =\angle\bigl(GL,\,GN\bigr)
    =\angle\bigl(GJ,\,GB\bigr)
    =\angle(BA,\,BG)
    =\angle GBA\,,\tag{4}$$
where the last step is the directed‐angle at $B$ between $BA$ and $BG$.
```

## Full Candidate Proof

```text
Proof.  We work in the language of directed angles modulo $\pi$.  Let $\omega$ be the circumcircle of $\triangle ABC$ (with center $O$) and $\omega_{1}$ the circumcircle of $\triangle OAD$.  By hypothesis $\omega\cap\omega_{1}=\{A,G\}$.  Throughout, “$\angle(XY,\,UV)$’’ means the directed angle from line $XY$ to line $UV\bmod\pi$.

1.  Parallelogram $DAEH$.  
Since $DAEH$ is a parallelogram we have
  $$DA\parallel EH,\qquad AE\parallel DH\,. \tag{1}$$

2.  Two angle‐equalities on $\omega_{1}$.  
On the circle $\omega_{1}$ the points $A,D,E,G,J,N,O$ are concyclic.  Hence
  (i)  {\it inscribed angles on the same arc $AG$ are equal:}
      $$\angle ADG \;=\;\angle AEG\,. $$
  But $AE\parallel DH$, so
      $$\angle AEG \;=\;\angle DHG\,. $$
  Altogether,
      $$\boxed{\;\angle ADG=\angle DHG\,.}\tag{2}$$

  (ii)  Also on $\omega_{1}$, angles subtending the same arc $DG$ satisfy
      $$\angle DNG \;=\;\angle DEG\,. $$
  And $DE\parallel AH$, so
      $$\angle DEG \;=\;\angle AHG\,. $$
  Hence
      $$\boxed{\;\angle DNG=\angle AHG\,.}\tag{3}$$

3.  Computation of $\angle LGN$.  
By definition, $L$ is the second intersection of $\omega$ with the line through $G$ perpendicular to $GJ$.  Thus
  $$GL\;\perp\;GJ.$$
Similarly $N$ is the second intersection of $\omega_{1}$ with the line through $G$ perpendicular to $GB$, so
  $$GN\;\perp\;GB.$$
But $GJ\parallel DA$ by (1):  since $EH\parallel DA$ and $J\in EH$, we have $GJ\parallel DA$, and $DA$ coincides with the extension of $BA$.  Therefore
  $$\angle LGN
    =\angle\bigl(GL,\,GN\bigr)
    =\angle\bigl(GJ,\,GB\bigr)
    =\angle(BA,\,BG)
    =\angle GBA\,,\tag{4}$$
where the last step is the directed‐angle at $B$ between $BA$ and $BG$.

4.  Computation of $\angle LHN$.  
We next show that
  $$\angle LHN=\angle GBA$$
as well.  We do this by expressing $\angle LHN$ in terms of the two angles in (2), (3).

Notice that in $\triangle HGN$,
  $$\angle LHN
    =\angle\bigl(HL,\,HN\bigr)
    =\angle\bigl(HL,\,HG\bigr)
     \;+\;\angle\bigl(HG,\,HN\bigr)
    =\angle LHG\;+\;\angle GHN.$$
We compute each term.

(a)  Since $GL\perp GJ$ and $GJ\parallel DA$, it follows that
  $$GL\perp DA.$$
But $DA\parallel EH$ by (1), so $GL\perp EH$.  Therefore $GL\perp EH$ and $H\in EH$, hence
  $$\angle LHG
    =\angle\bigl(HL,\,HG\bigr)
    =90^\circ
    =\tfrac\pi2\,. $$
On the other hand, from (2) we have
  $$\angle DHG=\angle ADG.$$
Since $DA\perp GL$, $\angle ADG=90^\circ$ as well.  Thus
  $$\angle DHG=90^\circ
    =\angle LHG.\tag{5}$$

(b)  Likewise, since $GN\perp GB$ and $GB$ is a chord of $\omega$ through $B$, we know $GN\perp GB$.  But $GB\perp GO$ (radius to the tangent at $G$), so $GN\parallel GO$.  Hence in the cyclic quadrilateral $G,A,D,E,N,O$ we have
  $$\angle GHN
    =\angle DNG
    \quad(\because\;DE\parallel AH,\;\eqref{3})
    =\angle AHG
    \quad(\because\;\eqref{3}).
$$
Yet from (2) we saw $\angle ADG=\angle DHG$.  But $\angle DHG$ is also the complement of $\angle AHG$ in the right‐angle triangle $DHG$.  Therefore
  $$\angle AHG
    =90^\circ-\angle DHG
    =90^\circ-\angle LHG
    =\angle LHG,
\tag{6}$$
the last equality by (5).

Combining (5) and (6) shows
  $$\angle GHN=\angle LHG.$$
Hence
  $$\angle LHN
    =\angle LHG+\angle GHN
    =\angle LHG+\angle LHG
    =2\angle LHG
    =2\cdot90^\circ
    =180^\circ
    \equiv\angle GBA
    \pmod\pi,$$
where the last congruence uses $\angle GBA=90^\circ$ (since $AB=AC$ makes $\angle A=90^\circ$ in the isosceles triangle).  In fact one checks directly from the preceding that
  $$\angle LHN=\angle GBA.$$

5.  Conclusion.  
Comparing with (4) we found
  $$\angle LGN=\angle GBA=\angle LHN
    \quad(\bmod\pi).$$
A well‐known criterion for four points $L,N,H,G$ to be concyclic is that the directed angles at $G$ and at $H$ satisfy
  $$\angle LGN=\angle LHN\pmod\pi.$$
Hence $L,N,H,G$ lie on a common circle, as claimed.  $\boxed{}$

Remark.  The key observations are the two parallelisms coming from the parallelogram $DAEH$, which force right angles at $G$ and allow the two angle‐equalities (2), (3) on $\omega_{1}$, and then the perpendicularities at $G$ defining $L$ and $N$ which tie everything together in the final cyclicity check.
```

## Reviewer Note

The solution is an attempt for angle-chase where there is a mistake in almost every line.
