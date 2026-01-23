# [Leetcode 994. Rotting Oranges][Link]

###### Medium

## Problem
You are given an `m x n` grid where:
- `0` represents an empty cell,
- `1` represents a fresh orange,
- `2` represents a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return the **minimum number of minutes** that must elapse until no cell has a fresh orange.  
If this is impossible, return `-1`.

<ins>_Example 1_</ins>:

**Input**:

```
grid = 
[[2,1,1],
[1,1,0],
[0,1,1]]
```


**Output**: `4`

---

## Steps to Solve:
- This problem is a classic **Breadth-First Search (BFS)** problem because:
  - Rotting spreads outward level by level.
  - Each level naturally represents **one minute of time**.

- First, scan the entire grid:
  - Add all initially rotten oranges to a queue.
  - Count how many fresh oranges exist.

- If there are **no fresh oranges at the start**, return `0` immediately since no time is needed.

- Use a queue to simulate the rotting process minute by minute:
  - Each iteration of the BFS represents **one minute**.
  - At the start of each minute, record the current size of the queue.
  - This ensures that only oranges rotten in the previous minute are processed.
  - Any newly infected oranges are added to the queue but processed in the next minute.

- For each rotten orange:
  - Check its four neighboring cells (up, down, left, right).
  - If a neighbor is a fresh orange:
    - Turn it rotten.
    - Decrease the fresh orange count.
    - Add it to the queue.

- Continue the process until:
  - The queue is empty, or
  - There are no fresh oranges left.

- After BFS finishes:
  - If all fresh oranges have rotted, return the number of minutes.
  - Otherwise, return `-1` because some oranges were unreachable.

**Key Insight**:  
By processing the queue **level by level**, we accurately simulate the passage of time and ensure each minute is counted correctly.

---

## Complexity
- `m`: number of rows in the grid  
- `n`: number of columns in the grid  

### Time: __O(m × n)__
- Each cell is visited at most once.
- BFS processes all oranges in linear time relative to the grid size.

### Space: __O(m × n)__
- The queue can contain up to all cells in the grid in the worst case.

[Link]: https://leetcode.com/problems/rotting-oranges/description/
