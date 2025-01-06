# [Leetcode 1672. Richest Customer Wealth][Link]

###### easy

## Problem
You are given an m x n integer grid accounts where `accounts[i][j]` is the amount of money the `ith` customer has in the `jth` bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum **wealth**.

 

_Example 1_:

**Input**: accounts = [[1,2,3],[3,2,1]]\
**Output**: 6\
**Explanation**:\
1st customer has wealth = 1 + 2 + 3 = 6\
2nd customer has wealth = 3 + 2 + 1 = 6\
Both customers are considered the richest with a wealth of 6 each, so return 6.

<br />

## Steps to Solve:
- use a `Sum function` like the `runningSum` in `#1480`
- loop through the `accounts array`, and send each customer's banks
  (each array of account array) to the function
- get the return output from the function and compare against the current max
- repeat the process and return the max

## Best solutions: 
- [Java][java]
  - [streams][java_streams]
  - [optionalInt][java_optionalInts]
- [Python][python]


## Complexity

- *Time*: __O(n * m)__
  - Traverse `n` customers
  - For each customer, traverse `m` banks
- *Space*: __O(1)__
  - Constant! We _**do not**_ create another data structure proportional
    in size of the input to help us find the solution


    







[Link]: https://leetcode.com/problems/richest-customer-wealth/description/
[java]: https://leetcode.com/problems/richest-customer-wealth/solutions/961720/java-1-liner-explained
[python]: https://leetcode.com/problems/richest-customer-wealth/solutions/2675823/python-1-liner-simple-solution
[java_streams]: https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html
[java_optionalInts]: https://docs.oracle.com/javase/8/docs/api/java/util/OptionalInt.html
