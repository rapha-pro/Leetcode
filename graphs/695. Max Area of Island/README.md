# [Leetcode 695. Max Area of Island][Link]

###### Medium

## Problem
You are given a 2D binary grid `grid` where:
- `1` represents land
- `0` represents water  

An island is formed by connecting adjacent lands **horizontally or vertically**.  
You may assume all four edges of the grid are surrounded by water.

Return the **maximum area of an island** in the grid.  
If there is no island, return `0`.

<ins>_Example 1_</ins>:

**Input**:

```
grid = 
[[0,0,1,0,0],
[0,1,1,1,0],
[0,0,1,0,0]]
```

**Output**: `5`

---

## Steps to Solve:
- Use **Depth-First Search (DFS)** to explore each island.
- First, get the number of rows and columns in the grid.
- Loop through every cell in the grid:
  - When a land cell (`1`) is found, it means we’ve discovered a new island.
  - Start a DFS from that cell to compute the total area of this island.

- **DFS traversal logic**:
  - If we go out of bounds, hit water (`0`), or reach a cell we’ve already visited, return `0`.
  - Otherwise:
    - Count the current land cell as `1`.
    - Mark it as visited so it is not counted again.
    - Recursively explore all four directions (up, down, left, right).
    - Add up the area returned by each recursive call.

- After finishing the DFS for one island:
  - Compare its area with the current maximum area.
  - Update the maximum if needed.

- Continue scanning the grid until all cells are processed.
- Return the maximum island area found.

**Key Details**:
- Marking visited cells (e.g., changing `1` to `-1`) prevents infinite loops and double counting.
- Each land cell is visited exactly once, ensuring efficiency.
- DFS naturally groups connected land cells into a single island.

---

## Complexity
- `r`: number of rows  
- `c`: number of columns  

### Time: __O(r × c)__
- Each cell is visited at most once.
- DFS explores each land cell exactly one time.

### Space: __O(r × c)__
- Worst-case recursion stack when the grid is filled entirely with land.
- No additional data structures are used besides recursion.

[Link]: https://leetcode.com/problems/max-area-of-island/description/
