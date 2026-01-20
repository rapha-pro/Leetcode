# [Leetcode Number of Islands][Link]

###### medium

## Problem


<ins>_Example 1_</ins>:

---
## Steps to Solve:
This is the **single most important graph pattern** to learn. If you master the logic behind **Number of Islands**, you effectively solve ~10 other popular LeetCode questions immediately (like *Max Area of Island*, *Flood Fill*, *Surrounded Regions*).

Here is the concept without code first, so you understand the "physics" of the problem.

### The Concept: "The Helicopter and the Sinking Island"

Imagine you are in a helicopter flying over a grid of ocean (`0`) and land (`1`). Your job is to count how many islands there are.

You scan the map from the **top-left** to the **bottom-right**, cell by cell.

#### The Algorithm in English
1.  **Scan:** You fly over the grid. If you see water (`0`), ignore it.
2.  **Discovery:** The moment you see land (`1`), you say: **"Found one!"** (Increment your island counter).
3.  **The trick (Flood Fill):** You don't just fly away. You land on that square. You run to every single piece of attached land (up, down, left, right) and **sink it** (mark it as `0` or "visited").
    *   Why? So that later, when your helicopter continues scanning the map, you don't count these pieces of land again. You've already "processed" this whole island.
4.  **Repeat:** Once that entire island is sunk/visited, you get back in the helicopter and continue scanning where you left off.

---

### Visual Walkthrough

Imagine this grid:
```text
1 1 0
1 0 0
0 0 1
```

**Step 1:** Helicopter starts at `(0,0)`. It sees a `1`.
*   **Action:** Count = 1.
*   **Trigger DFS/Flood Fill:**
    *   We are at `(0,0)`. Mark it visited (turn to `0`).
    *   Check neighbors.
    *   Right `(0,1)` is a `1`. Go there. Mark it visited.
    *   Down `(1,0)` is a `1`. Go there. Mark it visited.
    *   (All other neighbors are `0` or out of bounds).
*   **Result of Step 1:** The grid now looks like this to our "visited" tracker:
    ```text
    0 0 0  <-- (these used to be 1s, now processed)
    0 0 0
    0 0 1
    ```

**Step 2:** Helicopter continues scanning.
*   It looks at `(0,1)`, `(0,2)`, `(1,0)`... they are all `0` now (either originally water or sunk by us).
*   It ignores them.

**Step 3:** Helicopter reaches `(2,2)`. It sees a `1`.
*   **Action:** Count = 2.
*   **Trigger DFS/Flood Fill:**
    *   Sink `(2,2)`.
    *   No neighbors are land.
*   **Result:** Algorithm finishes.

**Total Islands: 2**

---

### The Pattern to Memorize

This pattern is called **"Loop + DFS"**.

1.  **Outer Loop:** Iterate through every cell `r` (row) and `c` (col).
2.  **Condition:** `if grid[r][c] == "1"`.
3.  **Action:**
    *   `count += 1`
    *   Call `dfs(r, c)`
4.  **Inside DFS:**
    *   **Base Case (Stop):** If out of bounds OR if current cell is water (`0`), return.
    *   **Process:** Mark current cell as water (`0`) so we don't visit it again.
    *   **Recursive Step:** Call DFS on up, down, left, right.

---

### Why this specific code structure?
1.  **`grid[r][c] = '0'`**: This saves us memory. Instead of creating a separate `visited` set (which costs O(N*M) space), we modify the input grid directly to mark things as visited.
    *   *Note: If the interviewer asks "What if the input is read-only?", then you use a `visited = set()`.*
2.  **The Base Case:** Notice how we check `r < 0` or `r >= rows` *first*. This prevents "Index Out of Bounds" errors. This is critical.

### How to apply this to other problems?
Now that you know this "Loop + DFS" pattern:

1.  **Max Area of Island:** instead of just `dfs(r,c)`, make it return `1 + dfs(up) + dfs(down)...` and track the `max`.
2.  **Count Connected Components:** Same logic, just a graph instead of a grid.
3.  **Flood Fill:** Same logic, but instead of sinking to `0`, you change color to `target_color`.

Do you feel comfortable with this logic? If so, I want you to try writing just the `dfs` function part of this code in your head (or scratchpad) right now.

---
## Complexity

- ### Time: __O(n)__
  - 
- ### Space: __O(n)__
  - 


    







[Link]: https://leetcode.com/problems/number-of-islands/
