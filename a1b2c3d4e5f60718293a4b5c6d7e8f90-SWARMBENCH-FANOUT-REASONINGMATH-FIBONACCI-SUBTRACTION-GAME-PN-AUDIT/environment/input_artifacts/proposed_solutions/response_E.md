This subtraction game can be solved using Sprague-Grundy theory.

Define:

[
g(n)=\operatorname{mex}{g(n-f)}
]

where (f) ranges over Fibonacci moves.

The move set is:

[
1,2,3,5,8,13,21,34,55,89
]

Now compute:

[
g(0)=0
]
[
g(1)=1
]
[
g(2)=2
]
[
g(3)=3
]
[
g(4)=0
]
[
g(5)=4
]

Continuing the mex table gives:

```text
0,1,2,3,0,4,1,2,3,4,0,1,2,3,0,4,1,2,3,4,0,1,2,3,0,4,1,2,3,4,0,1,2,3,0,4,1,2
```

Converting Grundy value 0 to P and all nonzero Grundy values to N, the first portion of the classification is:

```text
PNNNPNNNNNPNNNPNNN
```

So the final classification can be extended from this pattern.
