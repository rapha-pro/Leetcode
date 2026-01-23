# [Leetcode 1091. Shortest Path in Binary Matrix][Link]

###### Medium  
#### Related to Breadth-First Search (BFS), Matrix Traversal

## Problem
Given an `n x n` binary matrix `grid`, return the length of the **shortest clear path** from the top-left cell `(0,0)` to the bottom-right cell `(n-1,n-1)`.

A clear path:
- Only moves through cells with value `0`
- Can move in **8 directions** (horizontal, vertical, and diagonal)
- Includes both the starting and ending cells in the path length

Return `-1` if there is no clear path.

<ins>_Example 1_</ins>:

**Input**:
```
grid = 
[[0,1],
[1,0]]
```

**Output**: `2`

---

## Steps to Solve:
- This problem is a classic **shortest path** problem on a grid, which makes **Breadth-First Search (BFS)** the ideal approach.
  - BFS explores level by level, like ripples spreading on water.
  - The **first time** we reach the destination, we are guaranteed it’s the shortest path.

- Start by checking edge cases:
  - If the starting cell `(0,0)` or the destination cell `(n-1,n-1)` is blocked (`1`), no path exists → return `-1`.

- Use a queue to perform BFS:
  - Each element in the queue stores the current cell position and the path length taken to reach it.
  - The starting cell `(0,0)` begins with a path length of `1` (the starting cell counts).

- Define all **8 possible directions**:
  - Up, down, left, right
  - Four diagonals
  - These allow movement to all valid neighboring cells.

- While the queue is not empty:
  - Take the next cell from the queue.
  - If this cell is the destination, return its path length immediately.
  - Otherwise, explore all valid neighboring cells:
    - Stay within the grid boundaries.
    - Only move to cells with value `0` (clear path).
    - Mark visited cells as blocked (`1`) to avoid revisiting them.
    - Add each valid neighbor to the queue with an increased path length.

- If BFS completes without reaching the destination, return `-1`.

**Key Idea**:  
Because BFS explores all cells at distance `k` before moving to distance `k+1`, the first time we reach the bottom-right cell is guaranteed to be the shortest path.

---

## Complexity
- `n`: number of rows (and columns) in the grid

### Time: __O(n²)__
- In the worst case, every cell in the grid is visited once.
- For each cell, we check up to 8 neighbors.
- Total → **O(n²)**

### Space: __O(n²)__
- The queue can store up to `n²` cells in the worst case.
- The grid itself is reused to mark visited cells, avoiding extra memory.

[Link]: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
