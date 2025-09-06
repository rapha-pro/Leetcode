# [Leetcode 238. Product of Array Except Self][Link]

###### medium

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the 
elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and ***without using the division operation***.

<ins>_Example 1_</ins>:

**Input**: nums = [1,2,3,4]\
**Output**: [24,12,8,6]

**Explanation**:  
- For index 0: 2 * 3 * 4 = 24  
- For index 1: 1 * 3 * 4 = 12  
- For index 2: 1 * 2 * 4 = 8  
- For index 3: 1 * 2 * 3 = 6  

<ins>_Example 2_</ins>:

**Input**: nums = [-1,1,0,-3,3]\
**Output**: [0,0,9,0,0]

## Steps to Solve:
- Initialize three arrays of length `n`: `prefix`, `suffix`, and `output`, all filled with 1.  
- The **prefix array** will store the product of all elements **to the left** of each index.  
  - We loop from left to right starting at index 1 because the first element of prefix is always 1.  
  - This is because there are no elements to the left of the first index, and 1 is the multiplicative identity.  
  - For each index, we multiply the previous prefix product by the element immediately to its left in the original array.  
- 
- The **suffix array** will store the product of all elements **to the right** of each index.  
  - We loop from right to left starting at the second-to-last index because the last element of suffix is always 1.  
  - This is because there are no elements to the right of the last index, and again 1 is the multiplicative identity.  
  - For each index, we multiply the next suffix product by the element immediately to its right in the original array.  
- 
- The **final output array** is calculated by multiplying the corresponding prefix and suffix values for each index.  
  - This ensures that for each position, we get the product of all elements **except the element at that index itself**.  
- 
- Return the output array.

ex1: [ 1, 2, 3, 4]\

prefix: [ 1, 1, 2, 6] *\
suffix: [24, 12, 4, 1]

output: [24, 12, 8, 6]
## Complexity
- `n`: length of `nums` array

### Time: __O(n)__
- Constructing the prefix array → O(n)  
- Constructing the suffix array → O(n)  
- Computing the output array → O(n)  
- Total → O(n + n + n) = **O(n)**

### Space: __O(n)__
- `prefix` array → O(n)  
- `suffix` array → O(n)  
- `output` array → O(n)  
- Total → **O(3n) = O(n)**
    







[Link]: https://leetcode.com/problems/product-of-array-except-self/description/
