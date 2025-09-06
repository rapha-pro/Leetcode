# [Leetcode 125. Valid Palindrome][Link]

###### easy


## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.  
Alphanumeric characters include letters and numbers.  

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

<ins>_Example 1_</ins>:

**Input**: s = `"A man, a plan, a canal: Panama"`  
**Output**: `true`  

**Explanation**:  
After cleaning → `"amanaplanacanalpanama"`, which is a palindrome.

---

## Steps to Solve: (*Two Pointer Approach*)
- Use two pointers, one starting from the left (`left`) and one from the right (`right`).  
- Skip over any characters that are not alphanumeric (since they don’t matter for palindrome checking).  
  - Example: spaces, commas, and punctuation are ignored.  
- Compare the characters at the left and right pointers after converting them to lowercase.  
  - If they are different, return `false` immediately.  
  - If they are the same, move the pointers inward (`left + 1`, `right - 1`) and continue.  
- Continue until the pointers cross. If no mismatches were found, return `true`.  

**Alternative approach**:  
- Create a cleaned version of the string by removing all non-alphanumeric characters and converting everything to lowercase.  
- Compare the cleaned string with its reverse. If they are equal, it is a palindrome.  

---

## Complexity
- `n`: length of the string `s`

### Time: __O(n)__
- Each character is checked at most once (skipping or comparison).  
- String cleaning in the alternative approach also takes O(n).  

### Space:  
- **Two-pointer solution**: O(1) (only pointers used).  
- **Cleaning + reverse solution**: O(n) (extra string storage).  
    







[Link]: https://leetcode.com/problems/valid-palindrome/
