# [Leetcode 128. Longest Consecutive Sequence][Link]

###### medium

## Problem
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.  

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

* You must write an algorithm that runs in **O(n) time**.

<ins>_Example 1_</ins>:

**Input**: nums = `[100, 4, 200, 1, 3, 2]`  
**Output**: `4`  

**Explanation**: The longest consecutive sequence is `[1, 2, 3, 4]`, so its length is 4.

---

## Steps to Solve:
- Convert the input array into a **set** (`numSet`) for O(1) lookups.  
- Loop through every number `n` in the input array:  
  - First, check if `n` is the **start of a sequence**.  
    - This is true if `(n - 1)` is not in the set, meaning there is no smaller consecutive number before it.  
  - If it’s the start, we try to build the consecutive sequence beginning at `n`:  
    - Initialize a counter `length = 0`.  
    - While `(n + length)` is in the set, increase `length` by 1.  
    - This counts how long the consecutive chain continues forward.  
  - Update the global `longest_sequence` with the maximum between the current result and the newly found `length`.  
- After scanning all numbers, return `longest_sequence`.

**<ins>Key Detail</ins>**:  
We only attempt to build sequences when we are at the **smallest number of that sequence** (no left neighbor).  
This ensures each sequence is built only once, keeping the algorithm O(n).  

---
    
## Complexity
- `n`: number of elements in the input array  

### Time: __O(n)__
- Building the set → O(n)  
- Looping through each number → O(n)  
- Each sequence is checked only once because we only start from the smallest number in that sequence.\
  And we look up a number at most twice
- Total = **O(n)**  

### Space: __O(n)__
- Extra `set` to store all numbers → O(n)  






[Link]: https://leetcode.com/problems/longest-consecutive-sequence/description/
