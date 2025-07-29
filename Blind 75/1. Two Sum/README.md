# [Leetcode 1. Two Sum][Link]

###### easy

## Problem
Given an array of integers `nums` and an integer target, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

<ins>_Example 1_</ins>:

**Input**: nums = [2,7,11,15], target = 9 \
**Output**: [0,1] \
**Explanation**: \
Because nums[0] + nums[1] == 9, we return [0, 1].

## Steps to Solve:
- create a dictionary
- index iteration through the list of numbers
- for each number, find its difference to reach target
- check if that diff already exist in the hash map ( the dictionary with previous numbers as key and their indices in the num array as values)
- if it exists, return index of diff and the index of the current value which would just be i. (Won't obviously return at first iteration)


## Complexity

- *Time*: __O(n)__
  - We loop through the entire array
- *Space*: __O(n)__
  - In the worst case, we will need another data structure (in case: hashmap), with the same size as the input array


    







[Link]: https://leetcode.com/problems/two-sum/description/
