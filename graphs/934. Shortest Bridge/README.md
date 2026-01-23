# [Leetcode 934. Shortest Bridge][Link]

###### Medium  
#### Related to [Leetcode 200. Number of Islands][related_1], [Leetcode 1091. Shortest Path in Binary Matrix][related_2]

## Problem
You are given an `n x n` binary matrix `grid` where:
- `1` represents land
- `0` represents water  

There are **exactly two islands** in the grid.  
You may flip `0`s to `1`s to connect the two islands.

Return the **minimum number of 0s that must be flipped** to connect the two islands.

---

## Steps to Solve:

### Core Idea
- Use **DFS** to find and mark one entire island.
- Then use **BFS** to expand outward from that island until we reach the second island.
- The number of BFS layers expanded is the number of flips needed.

---

### Phase 1: Find and mark the first island (DFS)
- Loop through the grid to find the first land cell (`1`).
- Once found, perform a **DFS** to explore the entire island:
  - Mark every cell of this island as `2` to indicate it has been visited.
  - Store all these coordinates in a queue.
- Marking the island helps later:
  - When we encounter a `1` again, we know it belongs to the **second island**.
  - It also prevents revisiting the same cells.

---

### Phase 2: Expand outward to reach the second island (BFS)
- Use **BFS starting from all cells of the first island at once**.
- Each BFS layer represents flipping one `0` into land.
- For each cell in the queue:
  - Explore its 4-directional neighbors.
  - If a neighbor is `0`, flip it (mark as `2`) and add it to the queue.
  - If a neighbor is `1`, we’ve reached the second island — return the current distance.
- After processing one full BFS layer, increase the distance by 1.

---

### Why this works
- DFS ensures we correctly capture the entire first island.
- BFS guarantees the shortest path because it expands evenly in all directions.
- The first time we reach the second island is the minimum number of flips needed.

---

## Complexity
- `n`: number of rows (and columns) in the grid  

### Time: __O(n²)__
- DFS may visit all cells in the grid → O(n²)
- BFS may also expand across the grid → O(n²)
- Total → **O(n²)**

### Space: __O(n²)__
- Queue used for BFS can hold up to all grid cells.
- Recursion stack for DFS in the worst case.
- Grid is modified in-place to track visited cells.

---

[Link]: https://leetcode.com/problems/shortest-bridge/description/  
[related_1]: /graphs/200.%20Number%20of%20Islands
[related_2]: /graphs/1091.%20Shortest%20Path%20in%20Binary%20Matrix
