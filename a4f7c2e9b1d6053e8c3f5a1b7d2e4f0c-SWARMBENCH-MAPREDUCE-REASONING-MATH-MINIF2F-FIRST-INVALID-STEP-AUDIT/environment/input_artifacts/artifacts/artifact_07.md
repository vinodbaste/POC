# artifact_07

Competition: AIME
Problem ID: aime_1989_p4
Year: 1989

You are reviewing a proof attempt for a miniF2F benchmark problem. A curator extracted four candidate reasoning steps from an incorrect informal proof. Exactly one candidate step contains the **first** invalid or unjustified reasoning in this proof. Choose the correct option letter. The candidate steps are presented in randomized order (not necessarily in proof order).

## Problem

In how many ways can a committee of $3$ people be chosen from a group of $10$ people if two particular people, Alice and Bob, cannot both be on the committee?

## Candidate Excerpts

### Option A

```text
Total unrestricted committees of size 3 from 10 people: C(10,3) = 120.
```

### Option B

```text
The number of valid committees = 120 - 8 = 112.
```

### Option C

```text
Committees containing both Alice and Bob: we must choose 1 more person from the
remaining 8, giving C(8,1) = 8 such committees.
```

### Option D

```text
To count valid committees, we use complementary counting and note that among the
120 total committees those containing Alice and Bob are committees of the unordered
pair {Alice, Bob, x} for each of the 10 possible choices of x (since x can be any
of the 10 people, including Alice or Bob themselves to form a "triple"). The number
of forbidden committees is therefore 10, giving 120 - 10 = 110.
```

## Full Candidate Proof

```text
Step 1. Unrestricted: C(10,3) = 10!/(3!·7!) = 120.

Step 2. Forbidden (Alice and Bob both present): choose 1 from the remaining 8
people → C(8,1) = 8 forbidden committees.

Step 3. Using complementary counting, but now noting that the forbidden committees
are {Alice, Bob, x} for any x in the full group of 10 people (including Alice and
Bob themselves as choices for x). This gives 10 forbidden committees, so the answer
is 120 - 10 = 110.

Step 4. Correct answer via Step 2: 120 - 8 = 112.
```

## Reviewer Note

Option C (Step 3) is the first invalid step. It claims that the third member $x$ of a forbidden committee can be any of the 10 people, including Alice or Bob — but Alice and Bob are already fixed as the two specific members. The third person must be chosen from the remaining $10 - 2 = 8$ people. Allowing $x = $ Alice or $x = $ Bob would create committees with repeated members, which is nonsensical for a committee-selection problem. The correct count of forbidden committees is 8, not 10.
