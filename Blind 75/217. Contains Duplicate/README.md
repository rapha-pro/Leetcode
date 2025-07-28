# [Leetcode 217. Contains Duplicate][Link]

###### easy

## Problem
Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
and return `false` if every element is distinct.


<ins>_Example 1_</ins>:

**Input**: nums = [1,2,3,1]

**Output**: true

**Explanation**:
The element 1 occurs at the indices 0 and 3.

## Steps to Solve:
- Create a HashSet
- As we loop through the array, add the element in the hashset
- if we encounter, a duplicate, return false

## Complexity

- *Time*: __O(n)__
  - loop through the entire array once
- *Space*: __O(n)__
  - At worst case (all unique elements), we will need another datastructure as large as the\
    original array


    







[Link]: https://leetcode.com/problems/contains-duplicate/description/
