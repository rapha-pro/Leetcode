# [Leetcode 383. Ransom Note][Link]

###### easy

## Problem
Given two strings `ransomNote` and `magazine`, return `true` if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

<ins>_Example 1_</ins>:

**Input**: ransomNote = "aa", magazine = "aab"\
**Output**: true
## Steps to Solve:
- Check if `ransomNote` and `magazine` have the same length
- Loop through the letters of `magazine`. For each letter, track its count and store it in a hashmap
- Loop through the letters of `ransomNote`, check if it is contained in the hashmap.\
  return False if not contained or if the count of the letter is already 0; else decrease the count of the letter in the hashmap
- Repeat for all letters


## Complexity

- *Time*: __O(n)__
  - 
- *Space*: __O(1)__
  - 


    







[Link]: https://leetcode.com/problems/ransom-note/description/
