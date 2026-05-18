This is basically Nim with one pile, so we can use the XOR rule.

A position is losing when the Nim-sum is zero. Since there is only one pile, the Nim-sum is just the pile size. But because the allowed moves are powers of two, the XOR parity controls the outcome.

The powers of two flip the least significant bit, so the positions repeat modulo 2:

[
P,N,P,N,\dots
]

Thus the classification string is:

```text
PNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNPNP
```
