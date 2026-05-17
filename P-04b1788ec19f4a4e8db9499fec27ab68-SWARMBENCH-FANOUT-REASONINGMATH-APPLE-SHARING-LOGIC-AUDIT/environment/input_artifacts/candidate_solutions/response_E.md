# Candidate Response E

# Solution: Working Backwards

This is a sequential game that I'll solve using **backward induction**, analyzing what each person will do given rational play by the others.

## Person 3's Position (Last Mover)
Person 3 must take whatever remains. While they prefer to satisfy goal 1, they have no control over it - they're forced to take all remaining apples.

## Person 2's Position 
Knowing Person 3 will take the rest, Person 2 must choose $a_2$ such that:
- After Person 1 takes $a_1$ and Person 2 takes $a_2$, Person 3 gets $a_3 = 100 - a_1 - a_2$
- **Goal 1 requires**: $a_2$ must be strictly between $a_1$ and $a_3$ (to avoid being max or min)
- **Goal 2**: Maximize $a_2$ subject to Goal 1

For $a_2$ to be in the middle: 
$$a_1 < a_2 < 100 - a_1 - a_2$$

This simplifies to:
$$a_1 < a_2 < frac{100 - a_1}{2}$$

## Person 1's Position (First Mover)
Person 1 knows Person 2 will choose the maximum $a_2$ that satisfies the above constraint.

**Testing $a_1 = 32$:**
- Required range for Person 2: $32 < a_2 < 34$
- Person 2 takes: $a_2 = 33$ (the only integer in this range)
- Person 3 gets: $a_3 = 100 - 32 - 33 = 35$
- Check: $(32, 33, 35)$ - Person 2 has the middle value yes

**Testing $a_1 = 34$ (higher):**
- Required range for Person 2: $34 < a_2 < 33$ - **impossible!**
- Person 2 cannot satisfy Goal 1
- Any value Person 2 takes will either tie or be max/min

**Testing $a_1 < 32$:**
- Person 1 gets less while still allowing Person 2 to satisfy Goal 1
- Violates Person 1's Goal 2 (maximize apples)

## Answer

$$(A, B, C) = boxed{(32, 33, 35)}$$

Each person achieves their primary goal: none takes the most (35) or least (32), and given the constraints, these values maximize what each can take.
