# [Leetcode 412. Fizz Buzz][Link]

###### easy

## Problem
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.\
answer[i] == "Fizz" if i is divisible by 3.\
answer[i] == "Buzz" if i is divisible by 5.\
answer[i] == i (as a string) if none of the above conditions are true.

<ins>_Example 1_</ins>:\
**Input**: n = 5\
Output: ["1","2","Fizz","4","Buzz"]


## Steps to Solve:
- Initialize an array
- Iterate starting from `1` to `n` inclusive
- For each iteration, initialize an `empty string`
- If the current number is divisible by `3`, `append Fizz` to the string
- Likewise, if it's divisible by `5`, `append Buzz` to the string
- If none of the two options above are applicable, convert the number
  to a `String` data type and append it to the string
- Append the string to the array
- Reset the string and repeat


## Complexity

- *Time*: __O(n)__
  - We loop till n, so our time complexity is linear
- *Space*: __O(n)__
  - We create an array linearly proportional to the input size


    







[Link]: https://leetcode.com/problems/fizz-buzz/description/
