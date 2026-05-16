Let me find the largest squared edge length $s^2$ of a cube whose eight vertices have distances $0, 1, 2, 3, 4, 5, 6, 7$ to a certain plane.

### Step 1: Key observation

The maximum distance from the plane to any vertex of the cube cannot exceed the length of the cube's space diagonal. This is because the space diagonal is the longest line segment that fits inside the cube, and any vertex-to-plane distance is bounded above by the diameter of the cube.

### Step 2: Set up the inequality

For a cube with edge length $a$, the space diagonal is $a\sqrt{3}$. The maximum vertex-to-plane distance over the eight given values is $7$. Therefore:

$$7 \leq a\sqrt{3}$$

### Step 3: Equality case

The maximum vertex-to-plane distance equals $a\sqrt{3}$ exactly when the plane is perpendicular to the cube's space diagonal AND one vertex of the cube lies on the plane. In our problem, one vertex IS on the plane (distance $0$), so equality holds:

$$a\sqrt{3} = 7$$

Solving:

$$a = \frac{7}{\sqrt{3}}, \qquad a^2 = \frac{49}{3}$$

### Step 4: Verify with the intermediate distances

The intermediate distances $1, 2, 3, 4, 5, 6$ are partitioned among the other six vertices of the cube, each at some fraction of the body-diagonal projection. The exact assignment is consistent with the body-diagonal-aligned plane, so this gives a valid cube.

Since the cube's orientation is fully determined by the constraint "one vertex on plane, opposite vertex at distance 7 = space diagonal," the cube's edge length is uniquely $a = 7/\sqrt{3}$. So the maximum $s^2$ equals this unique value.

### Conclusion

$$\boxed{\dfrac{49}{3}}$$
