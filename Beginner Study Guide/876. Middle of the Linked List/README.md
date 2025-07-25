# [Leetcode 876. Middle of the Linked List][Link]

###### easy

## Problem
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

<ins>_Example 1_</ins>:

**Input**: head = [1,2,3,4,5]\
**Output**: [3,4,5]\
**Explanation**: The middle node of the list is node 3.

## Steps to Solve:
- Initialize two pointers at the beginning of the list.\
  The first pointer moves faster than the second one (middle pointer)
- We can notice that, for every two moves of the faster pointer, 
  middle pointer moves by one node to track the middle


## Complexity

- *Time*: __O(n)__
  - Linear since with have to loop through all the linked-list
- *Space*: __O(1)__
  - No extra memory proportional to our input is used


    







[Link]: https://leetcode.com/problems/middle-of-the-linked-list/description/
