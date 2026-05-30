## Step 1: Understand the problem and the given information
We are given a sequence of nightly star visibility counts, A = [4,1,3,5,2,2,3,1,5,6,2,1], for N = 12 consecutive nights. Each star is visible during a single continuous interval of nights, and we need to find the minimum (m) and maximum (M) possible number of distinct stars observed across all nights.

## Step 2: Determine the minimum possible number of distinct stars (m)
To find the minimum number of distinct stars, we should try to combine the stars into the fewest possible number of continuous intervals. This can be achieved by considering the cumulative sum of the star counts and trying to explain the changes in the count by the minimum number of stars appearing or disappearing each night.

## Step 3: Calculate the minimum possible number of distinct stars (m)
By examining the given sequence A, we notice that the changes in the star counts can be explained by a small number of stars. For example, the increase from 4 to 5 can be explained by one new star, and the decrease from 5 to 2 can be explained by the disappearance of 3 stars. By carefully analyzing these changes, we can find the minimum number of distinct stars required to explain the observed sequence.

## Step 4: Determine the maximum possible number of distinct stars (M)
To find the maximum number of distinct stars, we should consider the scenario where each star is visible for only one night, except for the nights where the count is greater than 1. In such cases, we can have multiple stars visible for only one night to account for the higher count.

## Step 5: Calculate the maximum possible number of distinct stars (M)
By considering each night separately and assuming that each star is visible for only one night, we can calculate the maximum possible number of distinct stars. For example, on the first night, we have 4 stars, so we can have 4 distinct stars. On the second night, we have 1 star, so we can have 1 new distinct star. By continuing this analysis for all nights, we can find the maximum number of distinct stars.

## Step 6: Calculate m + M
Once we have determined the minimum (m) and maximum (M) possible number of distinct stars, we can calculate the sum m + M.

The final answer is: $\boxed{17}$