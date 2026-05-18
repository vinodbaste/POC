If the pile is empty, then the current player has already avoided making a losing move. So I classify (0) as an N-position.

From there:

* 0 = N
* 1 = P
* 2 = P
* 3 = N
* 4 = P

This is just the normal recurrence but with the labels reversed from the usual convention.

The final string is:

```text
NPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPPNPP
```
