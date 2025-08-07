# [Leetcode 271. Encode and Decode Strings][Link]

###### Medium

## Problem
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement `encode` and `decode`

<ins>_Example 1_</ins>:

**Input**: ["neet","code","love","you"]

**Output**:["neet","code","love","you"]


## Steps to Solve:

+ <ins>**General Idea**</ins>:
    + We need to **encode a list of strings into one string**, and then **decode it back**.
    + The challenge is to handle cases where strings may contain special characters like `#`, so we need a reliable way to separate them.

+ <ins>**Encoding Strategy**</ins>:
    + For each string, prefix it with its **length**, followed by a delimeter, which in this case is `#`, then the string itself.
    + Example: `"hello"` becomes `"5#hello"`.
    + Even if the following string started with the delimeter character, `#`, we just read the first one that directly
      follows the number.
        + For example: If the string was `#hello` instead of `hello`, the encoded string would be: `6##hello`
        + We would just read the first `#` symbol as the delimeter
    + Concatenate all such encoded strings into one long string.

+ <ins>**Decoding Strategy**</ins>:
    + Start from the beginning of the encoded string.
    + Read characters until you hit `#`—this gives you the **length** of the next word.
    + Use that length to extract the word that follows.
    + Repeat until the entire string is processed.

---

## Complexity

- ### Time: __O(n)__
    - Encoding: We loop through each string and build the result → `O(n)` where `n` is the total number of characters.
    - Decoding: We scan through the encoded string once → also `O(n)`.

- ### Space: __O(n)__
    - We store the encoded string and the decoded list, both proportional to the input size.








[Link]: https://neetcode.io/problems/string-encode-and-decode?list=blind75
