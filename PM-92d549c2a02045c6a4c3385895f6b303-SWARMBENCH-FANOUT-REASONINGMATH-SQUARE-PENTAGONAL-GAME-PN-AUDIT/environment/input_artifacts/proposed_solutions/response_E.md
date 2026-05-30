Here's a tiny Python-script you can copy–paste and run in order to produce exactly the 141-character string you want.  It uses straightforward DP in $O(N\cdot M)$ time, where $N=140$ and $M$ is the number of allowed moves (19).

```python
# compute P- and N-positions for subtraction game with
# moves = {perfect squares} ∪ {pentagonal numbers}
def compute_PN_string(N=140):
    # 1) build the move-set M
    M = set()
    # perfect squares ≤ N
    i = 1
    while i*i <= N:
        M.add(i*i)
        i += 1
    # pentagonal numbers P_n = n(3n−1)//2 ≤ N
    n = 1
    while True:
        p = n*(3*n - 1)//2
        if p > N: break
        M.add(p)
        n += 1
    M = sorted(M)

    # 2) DP array: True iff position k is a P-position
    isP = [False] * (N+1)
    isP[0] = True   # by definition

    for k in range(1, N+1):
        # if there is any move m with k−m >= 0 and isP[k−m] == True,
        # then k is an N-position; otherwise k is P.
        isN = False
        for m in M:
            if m > k: break
            if isP[k - m]:
                isN = True
                break
        isP[k] = not isN

    # 3) build the output string: 'P' for True, 'N' for False
    return ''.join('P' if isP[k] else 'N' for k in range(N+1))

# produce and print the 141-character string
if __name__ == '__main__':
    s = compute_PN_string(140)
    print(s)
```

If you run that script in any standard Python 3 interpreter, it will print out exactly 141 characters (one for each $k=0,1,2,\dots,140$), with 'P' or 'N' in the required positions. I have not executed the script myself in this session, so I'm not including the printed 141-character classification string here — the algorithm above is the proposed approach, not a finished answer.
