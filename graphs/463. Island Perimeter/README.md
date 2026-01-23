# [Leetcode 463. Island Perimeter][Link]

###### Easy

## Problem
You are given a 2D grid representing a map, where:
- `1` represents land
- `0` represents water

There is exactly **one island** in the grid (one connected component of land), and the island does not have any lakes (water inside the island).

Return the **perimeter of the island**.

<ins>_Example 1_</ins>:

**Input**:

```
grid = 
[[0,1,0,0],
[1,1,1,0],
[0,1,0,0],
[1,1,0,0]]
```

**Output**: `16`

---

*Key Insight*: Can be solved without DFS, can you find how?
*Hint: what happens to the perimeter when two cells (piece of land) touch each other?*

## Steps to Solve:
- Since there is exactly **one island**, we only need to find **one land cell** and traverse the entire island.
- We use **Depth-First Search (DFS)** to explore all connected land cells.
- The key idea is to compute the perimeter by counting **edges that touch water or go out of bounds**.

### DFS intuition:
- Every land cell has 4 sides.
- A side contributes to the perimeter **if it touches water or the edge of the grid**.
- While traversing the island, each DFS call explores all 4 directions (up, down, left, right).

### Base cases during DFS:
- **Out of bounds or water (`0`)**  
  - This means we hit the boundary of the island.
  - That edge contributes **+1 to the perimeter**.
- **Already visited land**  
  - This cell has already been processed.
  - It contributes **0** to the perimeter to avoid double-counting.

### Traversal logic:
- When we visit a land cell:
  - Mark it as visited (by modifying the grid value).
  - Recursively explore all four neighboring directions.
  - Sum up the perimeter contributions returned from each direction.

### Main loop:
- Scan the grid to find the **first land cell**.
- Since there is only one island, start DFS from there and return the result immediately.

---

## Complexity
- `rows`: number of rows in the grid  
- `cols`: number of columns in the grid  

### Time: __O(rows × cols)__
- In the worst case, every cell is visited once.
- Each DFS call does constant work.

### Space: __O(rows × cols)__
- Recursive DFS call stack in the worst case.
- Grid is modified in-place to mark visited cells.

[Link]: https://leetcode.com/problems/island-perimeter/description/
