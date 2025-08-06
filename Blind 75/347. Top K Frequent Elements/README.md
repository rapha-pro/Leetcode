# [Leetcode 347. Top K Frequent Elements][Link]

###### Medium

## Problem
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

<ins>_Example 1_</ins>:

**Input**: nums = [1,1,1,2,2,3], k = 2\
**Output**: [1,2]


## Steps to Solve:

+ <ins>General Idea</ins>:
  + We want to find the `k` most frequent elements in a list.
  + First, count how often each number appears.
  + Then, group numbers by their frequency.
  + Finally, collect the top `k` frequent numbers by scanning from highest frequency to lowest.

+ <ins>Bucket Sort Method</ins>:
  + Create a dictionary to count frequency of each number.
  + Create a list of buckets, where each index `i` holds numbers that appear `i` times.
  + Since the maximum frequency can't exceed the length of the list, we make `len(nums) + 1` buckets.
  + Traverse the buckets in reverse (from high frequency to low), collecting numbers until we have `k`.

---

## Complexity

- ### Time: __O(n)__  
  - Counting frequencies takes `O(n)` time.
  - Filling buckets also takes `O(n)` time.
  - Scanning buckets to collect top `k` elements is at most `O(n)` in the worst case.
  - So overall, it's linear time: `O(n)`.

- ### Space: __O(n)__  
  - We use a dictionary to store frequencies: `O(n)` space.
  - We use a list of buckets: `O(n)` space.
  - The result list takes up to `k` space, which is ≤ `n`.





[Link]: https://leetcode.com/problems/top-k-frequent-elements/description/
