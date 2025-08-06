# [Leetcode 49. Group Anagrams][Link]

###### Medium

#### Related to [Leetcode 242. Valid Anagram][related_question]

## Problem
Given an array of strings strs, group the anagrams together. You can return the answer in 
any order.Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

<ins>_Example 1_</ins>:

**Input**: strs = `["eat","tea","tan","ate","nat","bat"]`

**Output**: `[["bat"],["nat","tan"],["ate","eat","tea"]]`

**Explanation**:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

## Steps to Solve:
- Valid anagrams have `thesame` frequency for each character
- create a dictionary
- Loop through every `string 's'` in the `strs` array
- Initialize an int array (filled with 0) for each letter of the alphabet to store the count of each letter
- For each element at its index (e.g: a, has index = 0, b = 1, c = 2, etc..), update its count as seen in `string 's'`
- Use this array (converted to a string) as the key for the dictionary, and its values would be a 
  list of all anagrams of the `current string 's'`
- i.e: For each string, after creating its array frequency, check if exists already in the dictionary, \
  and add the current string as array `value` that is paired with the current `key`, else insert this key-value pair \
  to the dict

## Complexity

- `m`: the length of the array `strs`. 
- `n`: average or worst length of a string in `strs`
- 
- ### Time: __O(m * n)__
  - `O(m * n * 26)`. For every string in `strs (m)`, we loop through each letters of the string (`n`), and create
    an array of size `26`.
  - since for any input, the string of the array is constant (26), it is not included in the time complexity
- ### Space: __O(m * n)__
  - O(m * n) space complexity represents the total number of characters stored across all input strings in the worst case
  - In the worst case, we will need a dictionary with `m` arrays, each of length `26` = `26m`
  - But, the map itself holds n entries → `O(m) keys + O(m) lists`.
  - `m` strings, each of length up to `n`, stored in lists.
    - Key: `[1,1,0,...]` → ["bat", "tab"]
    - Key: `[1,0,1,...]` → ["eat", "tea"]
    - Key: `[1,0,0,...]` → ["tan", "nat"]
    - 3 keys → O(3)
    - 6 strings stored → `O(6 * 3) = O(18)` characters → `O(m * n)`





    







[Link]: https://leetcode.com/problems/group-anagrams/description/
[related_question]: /Blind%2075/242.%20Valid%20Anagram