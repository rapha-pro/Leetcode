# [Leetcode 419. Battleships in a Board][Link]

###### Medium

## Problem
Given an `m x n` board where each cell is either `'X'` (part of a battleship) or `'.'` (empty), return the number of battleships on the board.

Battleships can only be placed **horizontally or vertically**, and they are separated by at least one empty cell (`'.'`).

You must count battleships **without modifying the board** and using **O(1) extra space**.

<ins>_Example 1_</ins>:

**Input**:

```
[["X",".",".","X"],
[".",".",".","X"],
[".",".",".","X"]]
```

**Output**: `2`

---

## Steps to Solve:
- Initialize a counter to keep track of how many battleships are found.
- Traverse the board cell by cell using two nested loops (row by row, column by column).
- Every time we encounter an `'X'`, we check whether it is the **start of a new battleship**.
- A cell is considered the start of a battleship if:
  - There is **no `'X' directly above it** (meaning it is not continuing a vertical ship), and
  - There is **no `'X' directly to the left of it** (meaning it is not continuing a horizontal ship).
- If either of those conditions is false, then the current `'X'` is part of a battleship we have already counted, so we skip it.
- If both conditions are satisfied, this `'X'` represents the **top-left-most cell** of a new battleship, and we increment the counter.
- Continue scanning until the entire board has been processed.
- Return the final count.

**Key Insight**:  
By only counting battleships at their starting position (topmost or leftmost cell), we avoid double-counting ships that span multiple cells.

---

## Complexity
- `m`: number of rows  
- `n`: number of columns  

### Time: __O(m × n)__
- Every cell in the board is visited exactly once.

### Space: __O(1)__
- Only a counter is used.
- No extra data structures are required.

[Link]: https://leetcode.com/problems/battleships-in-a-board/description/
