# [Leetcode 1480. Running Sum of 1D Array][Link]

###### easy

## Problem
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of nums.

_Example 1_:

**Input**: nums = [1,2,3,4]\
**Output**: [1,3,6,10]\
**Explanation**: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]. 
<br /><br />

## Steps to Solve:

- Start an iteration from the `second element`
- add the `previous element` to the current one
- move on and repeat the process



## Complexity

- *Time*: __O(n)__
  - We perform thesame number of operations on each element (adding running sum),
    as we loop through the array once
- *Space*: __O(1)__
  - Constant because we do not include the space used by our input array.
  - No extra memory proportional to our input is used


    







[Link]: https://leetcode.com/problems/running-sum-of-1d-array/description/
