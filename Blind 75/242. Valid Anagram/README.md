# [Leetcode 242. Valid Anagram][Link]

###### easy

#### Related to [Leetcode 383. Ransom Note][related_question]

## Problem
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

<ins>_Example 1_</ins>:

**Input**: s = "anagram", t = "nagaram"

**Output**: true

## Steps to Solve:
- check if both string have the same length
- initialize an int array (filled with 0) for each letter of the alphabet to store the count of each letter 
- For each element at its index (e.g: a, has index = 0, b = 1, c = 2, etc..), update its count as seen in string `s`
- Loop through each character of the other string `t`, and check if the count = 0, then return `false` \
  else decrease the count


## Complexity

- *Time*: __O(n + m)__
  - we loop through all the characters of both string
- *Space*: __O(1)__
  - The maximum size of the array is the number of characters in the alphabet no matter the input size\
    therefore it's constant


    







[Link]: https://leetcode.com/problems/valid-anagram/description/
[related_question]: /Beginner%20Study%20Guide/383.%20Ransom%20Note
