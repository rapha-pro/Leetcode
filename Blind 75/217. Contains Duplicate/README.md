# [Leetcode 217. Contains Duplicate][Link]

###### easy

## Problem
Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
and return `false` if every element is distinct.


<ins>_Example 1_</ins>:

**Input**: nums = [1,2,3,1]

**Output**: true

**Explanation**:
Element 1 occurs at the indices 0 and 3.

## Steps to Solve:
- Create an integer set
- As we loop through the array, first check if the current element is already contained in the set
- Return `true` if contained, else add the element to the set.
- If we successfully exit the loop, return `false`.

## Complexity

- *Time*: __O(n)__
  - Loop through the entire array once
- *Space*: __O(n)__
  - In the worst case (all unique elements), we will need another data structure as large as the input array


    







[Link]: https://leetcode.com/problems/contains-duplicate/description/
