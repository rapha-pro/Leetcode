# [Leetcode 394. Decode String][Link]

###### Medium

## Problem
Given an encoded string `s`, return its decoded string.

The encoding rule is:  
`k[encoded_string]`, where the `encoded_string` inside the square brackets is repeated exactly `k` times.  

You may assume that:
- The input string is always valid.
- There are no extra spaces.
- Numbers can be multiple digits.

<ins>_Example 1_</ins>:

**Input**: s = `"3[a]2[bc]"`  
**Output**: `"aaabcbc"`

---

## Steps to Solve:
- Use a **stack** to process the string character by character.  
  The stack helps us keep track of characters, numbers, and nested structures until we can fully decode them.

- Traverse the string from left to right:
  - If the current character is **not a closing bracket `]`**, push it onto the stack.
  - This includes digits, letters, and opening brackets `[`.

- When a closing bracket `]` is encountered:
  - Start building the **substring inside the brackets** by popping characters from the stack.
  - Keep popping until the matching opening bracket `[` is found.
  - This gives the encoded substring that needs to be repeated.
  
- After removing the opening bracket:
  - Extract the number (`k`) that appears just before it.
  - Since numbers can have multiple digits, keep popping digits from the stack until a non-digit is found.
  - Convert this number into an integer.

- Repeat the decoded substring `k` times and push the resulting string back onto the stack.
  - This allows nested encoded strings to be handled naturally.

- Continue this process until the entire string has been processed.

- Finally, join everything left in the stack to form the fully decoded string.

**Key Insight**:  
The stack ensures that **inner brackets are decoded before outer ones**, which makes it ideal for handling nested encoded strings like `"3[a2[c]]"`.

---

## Complexity
- `n`: length of the input string `s`

### Time: __O(n)__
- Each character is pushed and popped from the stack at most once.
- String construction happens proportionally to the final decoded output.
- Overall → **O(n)**.

### Space: __O(n)__
- Stack can grow up to the size of the input string.
- Extra space is also used to store intermediate decoded substrings.

[Link]: https://leetcode.com/problems/decode-string/description/
