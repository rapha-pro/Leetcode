# [Leetcode 383. Ransom Note][Link]

###### easy

## Problem
Given two strings `ransomNote` and `magazine`, return `true` if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in `magazine` can only be used once in `ransomNote`.

<ins>_Example 1_</ins>:

**Input**: ransomNote = "aa", magazine = "aab"\
**Output**: true
## Steps to Solve:
- Check if `magazine` have a shorter length than `ransomNote`
- Loop through the letters of `magazine`. For each letter, track its count and store it in a hashmap\
  (`key`: characters, `Values`: frequency)
- Loop through the letters of `ransomNote`, check if it is contained in the hashmap.\
  return False if not contained or if the count of the letter is already 0; else decrease the count of the letter in the hashmap
- Repeat for all letters


## Complexity

- ### Time: __O(n + m)__
  1. **Counting frequencies of the magazine** 
     - Loop through each character in the magazine string: `O(n)`
     - For each character, update its count in a hash map: `O(1)` 
     - Total = `O(n)`
  2. **Checking the ransom note**
     - Loop through each character in the ransom note: `O(m)`
     - For each character, check if the count in the hash map is sufficient: `O(1)`
     - Total = `O(m)`
     
- ### Space: __O(k.log n)__
  1. `k`: Number of unique characters. Since we're dealing with lowercase English letters, this is fixed: 26 
  2. The maximum count for a character is `n` (length of the string of magazine)
  3. Storing a number up to `n` requires logarithmic space in bits: `O(log n)`
     - String: `"aaaaaaaab"`
     - Length of the string: `n = 8`
     - The frequency of `'a'` is `7` & The frequency of `'b'` is `1`.
     - To store the number 7 in binary:
       - Binary form of 7: `111`
       - It takes `3` bits to store the number 7 = `2^3 - 1`
     - To store the number 1 in binary:
       - Binary form: `1`
       - It takes `1` bit = `2^1 - 1`
       - Therefore, n = 2^b - 1; `b = log₂(n-1)`
     - Because the largest count can be as big as `n` in the _worst case_, storing this count requires about `log₂ n` bits
    

- ### [Alternative Solution2 using array][alternative_sol]





[Link]: https://leetcode.com/problems/ransom-note/description/
[alternative_sol]: https://leetcode.com/problems/ransom-note/solutions/1671552/1ms-100-easy-explanation-java-solution
