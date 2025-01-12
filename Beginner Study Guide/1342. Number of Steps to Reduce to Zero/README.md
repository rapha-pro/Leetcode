# [Leetcode 1342. Number of Steps to Reduce a Number to Zero][Link]

###### easy

## Problem
Given an integer `num`, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by `2`,
otherwise, you have to subtract `1` from it.

<ins>_Example 1_</ins>: \
**Input**: num = 14 \
**Output**: 6 \
**Explanation**:\
Step 1) 14 is even; divide by 2 and obtain 7. \
Step 2) 7 is odd; subtract 1 and obtain 6.\
Step 3) 6 is even; divide by 2 and obtain 3. \
Step 4) 3 is odd; subtract 1 and obtain 2. \
Step 5) 2 is even; divide by 2 and obtain 1. \
Step 6) 1 is odd; subtract 1 and obtain 0.

## Steps to Solve:

+ <ins>General Way</ins>:
  + The Algorithm is outlined for us in this question, we just have
  to follow the steps.
+ <ins>Bitwise Method</ins>:
  + An integer that we use for the location of its bits, rather
    than its value
  + The last bit of all odd numbers end with 1 while evens ends with `0`
  + Use `1` as bitmask with the `&` operator to check if the last digit is 1
  + To divide in bit operations, `right-shift` by `1` all bits.
    The reverse is true for multiplication. \
    This is because each bit from right to left goes in increasing powers of 2


## Complexity

- *Time*: __O(log(n))__
  - Since we are constantly dividing by `2`, our time complexity is `log(n)`,
    which is the definition of a logarithm (number of steps required to divide
    a number by the base until it reaches 1)
  - In the worst case scenario (e.g #30), for half of the steps we divide by 2, (log n times)
  - For the other half, we subtract 1 (log n)
  - So the combine, `log n + log n`, we get `2 log n`
- *Space*: __O(1)__
  - No extra space used!










[Link]: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
