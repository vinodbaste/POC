# Response F

We compute positions recursively.

* A position is P if every legal move goes to an N.
* A position is N if at least one legal move goes to a P.

Allowed moves are: 1, 3, 4, 6, 9, 10, 15, 16, 21, 25, 28, 36, 45, 49, 55, 64, 66, 78, 81, 91, 100, 105, 120, 121

Starting from 0:

* 0 = P
* 1 = N
* 2 = P
* 3 = N

Continuing this recursion up to 130, we obtain:

```
PNPNNNNPNNNPNPNNNNNPNNNPNNNNNPNPNNNNNPNNNPNNNNNPNNNNNPNPNNNPNNNNNPNNNPNPNNNNNPNNNPNNNNNPNPNNNNNPNNNPNNNNNPNNN
```
