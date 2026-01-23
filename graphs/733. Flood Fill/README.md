# [Leetcode 733. Flood Fill][Link]

###### Easy

## Problem
An image is represented by an `m x n` integer grid `image`, where `image[r][c]` represents the color of a pixel.

You are given a starting pixel `(sr, sc)` and a new `color`.  
Perform a **flood fill** on the image starting from `(sr, sc)`.

The flood fill should:
- Change the color of the starting pixel and
- Change the color of all **4-directionally connected pixels** that have the same original color as the starting pixel.

Return the modified image.

<ins>_Example 1_</ins>:

**Input**:
```
image = 
[[1,1,1],
[1,1,0],
[1,0,1]]

sr = 1, sc = 1, color = 2
```

**Output**:

```
[[2,2,2],
[2,2,0],
[2,0,1]]
```

---

## Steps to Solve:
- This problem can be solved using **Depth-First Search (DFS)**, starting from the source pixel.
- First, store the **original color** of the starting pixel.
  - Only pixels with this color should be repainted.

- Define a recursive DFS function that:
  - Stops if the current position is:
    - Out of bounds, or
    - Already painted with the new color, or
    - Not the same color as the source pixel.
  - Otherwise:
    - Repaint the current pixel with the new color.
    - Recursively apply the same logic to its four neighbors (up, down, left, right).

- Start the DFS from `(sr, sc)`.
- Once the DFS finishes, all connected pixels of the same original color will be repainted.
- Return the modified image.

**Key Insight**:  
The DFS ensures that only pixels connected to the starting pixel **and sharing the same original color** are filled, preventing unintended color changes.

---

## Complexity
- `m`: number of rows in the image  
- `n`: number of columns in the image  

### Time: __O(m × n)__
- In the worst case, every pixel is visited once.

### Space: __O(m × n)__
- Recursive DFS stack can grow to the size of the image in the worst case.

[Link]: https://leetcode.com/problems/flood-fill/description/
