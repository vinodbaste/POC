# artifact_28

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
7.  Checking perpendicularity.  
  The slope of YZ is
    m_{YZ}
    = ( Z_y − Y_y )/( Z_x − Y_x )
    = ( c/(a+1) − 0 ) / ( b/(a+1) − c₀/(a+c₀) )
    =  [ c/(a+1) ]  /  [ (b(a+c₀) − c₀(a+1))/( (a+1)(a+c₀) ) ]
    =  c(a+1)(a+c₀) / [ (a+1)(b(a+c₀) − c₀(a+1)) ]
    =  c(a+c₀) / ( b(a+c₀) − c₀(a+1) ).
```

### Option B

```text
6.  The intersection P of lines I_BF and I_CE.  
  Parametrize  
    I_BF:  X = I_B + t·(F − I_B),
    I_CE:  X = I_C + s·(E − I_C).
  Equating gives two linear equations in s,t which one solves by Cramer’s rule.  We obtain after simplification
    P = ( x_P , y_P )
  where x_P and y_P are explicit rational functions of b,c,a,c₀.  (The formulas are too long to reproduce in full here, but they are elementary.)
```

### Option C

```text
The slope of OP is
    m_{OP}
    = ( y_P − O_y ) / ( x_P − O_x )
    = ( y_P − (c₀²−b)/(2c) ) / ( x_P − ½ ).
```

### Option D

```text
One then verifies by direct algebra that
    m_{YZ} · m_{OP} = −1.
  (All denominators clear, and one uses only the identities
     a² = (b−1)² + c²,
     c₀² = b² + c²,
   plus routine expansion and cancellation.)
```

## Full Candidate Proof

```text
Proof.  We begin by putting the triangle into a convenient Cartesian coordinate system and then verifying the perpendicularity by a straightforward (if somewhat lengthy) computation.

1.  Coordinate setup.  
  Without loss of generality place  
    A = (0,0),    C = (1,0),  
  and let B = (b,c) with c≠0 (so that triangle ABC is nondegenerate and acute).  Denote  
    AB=c₀=√(b²+c²),    BC=a=√((b−1)²+c²),    CA=1.  

2.  The feet of the altitudes.  
  –  E is the foot of the perpendicular from B to AC (the x-axis), hence  
      E=(b,0).  
  –  F is the foot of the perpendicular from C=(1,0) to the line AB through (0,0) and (b,c).  
     A standard projection formula gives  
      F = (( (1,0)·(b,c) )/(b²+c²))·(b,c)
        = ( b/(b²+c²)·b , b/(b²+c²)·c )
        = ( b²/c₀² , b c /c₀² ).  

3.  The points Y and Z on the sides via the angle-bisector theorem.  
  –  Y is where the internal bisector of ∠ABC meets AC; by the Angle-Bisector Theorem,  
      AY : YC = AB : BC = c₀ : a,  
    so  
      Y = ( c₀/(a+c₀) , 0 ).  
  –  Z is where the internal bisector of ∠ACB meets AB; by the same theorem,
      AZ : ZB = AC : BC = 1 : a.
    Since AB has length c₀, it follows
      Z = ( 1/(a+1) )·B = ( b/(a+1) , c/(a+1) ).  

4.  The circumcenter O of ABC.  
  The perpendicular bisector of AC (from (0,0) to (1,0)) is x=½.  Imposing OA²=OB² gives  
    (½)·b + O_y·c = (b²+c²)/2,
  so
    O = ( ½ , (c₀² − b)/(2c) ).  

5.  The B– and C–excenters in Cartesian form.  
  It is well known (or one may check by intersecting the external bisector at B with the internal bisectors at A and C) that the B–excenter I_B has barycentric coordinates (BC:CA:AB)=(a:−1:c₀) and hence in Cartesian coordinates
    I_B = ( (0·a + (b)(−1) + (1)·c₀)/(a−1+c₀) , (0·a + c·(−1) +0·c₀)/(a−1+c₀) )
         = ( (c₀−b)/(a−1+c₀) , −c/(a−1+c₀) ).
  Similarly the C–excenter I_C = (a:1:−c₀) gives
    I_C = ( (0·a + b·1 +1·(−c₀))/(a+1−c₀) , (0·a + c·1 +0·(−c₀))/(a+1−c₀) )
         = ( (b−c₀)/(a+1−c₀) ,  c/(a+1−c₀) ).  

6.  The intersection P of lines I_BF and I_CE.  
  Parametrize  
    I_BF:  X = I_B + t·(F − I_B),
    I_CE:  X = I_C + s·(E − I_C).
  Equating gives two linear equations in s,t which one solves by Cramer’s rule.  We obtain after simplification
    P = ( x_P , y_P )
  where x_P and y_P are explicit rational functions of b,c,a,c₀.  (The formulas are too long to reproduce in full here, but they are elementary.)  

7.  Checking perpendicularity.  
  The slope of YZ is
    m_{YZ}
    = ( Z_y − Y_y )/( Z_x − Y_x )
    = ( c/(a+1) − 0 ) / ( b/(a+1) − c₀/(a+c₀) )
    =  [ c/(a+1) ]  /  [ (b(a+c₀) − c₀(a+1))/( (a+1)(a+c₀) ) ]
    =  c(a+1)(a+c₀) / [ (a+1)(b(a+c₀) − c₀(a+1)) ]
    =  c(a+c₀) / ( b(a+c₀) − c₀(a+1) ).  

  The slope of OP is
    m_{OP}
    = ( y_P − O_y ) / ( x_P − O_x )
    = ( y_P − (c₀²−b)/(2c) ) / ( x_P − ½ ).

  One then verifies by direct algebra that
    m_{YZ} · m_{OP} = −1.
  (All denominators clear, and one uses only the identities
     a² = (b−1)² + c²,
     c₀² = b² + c²,
   plus routine expansion and cancellation.)  

Therefore OP is perpendicular to YZ, as claimed.  □
```

## Reviewer Note

Skipping calculation steps
