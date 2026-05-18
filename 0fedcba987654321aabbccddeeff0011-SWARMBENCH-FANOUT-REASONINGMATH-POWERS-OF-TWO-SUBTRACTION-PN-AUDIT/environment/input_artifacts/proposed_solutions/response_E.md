I will compute Sprague-Grundy numbers.

For a pile of size (n),

[
G(n)=\operatorname{mex}{G(n-1),G(n-2),G(n-4),G(n-8),G(n-16),G(n-32),G(n-64)}.
]

Starting values:

[
G(0)=0
]
[
G(1)=1
]
[
G(2)=2
]
[
G(3)=0
]
[
G(4)=3
]
[
G(5)=1
]
[
G(6)=2
]
[
G(7)=0
]

So the sequence of Grundy values begins:

```text
0,1,2,0,3,1,2,0,4,1,2,0,3,1,2,0,5,1,2,0,3,1,2,0,4,1,2,0,3,1,2,0
```

Converting these Grundy values to P/N where (G(n)=0) means P and all nonzero values mean N, the partial classification is:

```text
PNNPNNPNPNNPNNPNPNNPNNPNPNNPNN
```
