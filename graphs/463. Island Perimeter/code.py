from typing import List, Set, Tuple

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # using DFS
        rows, cols = len(grid), len(grid[0])
        visited: Set[Tuple[int, int]] = set()

        def islandTraversal(row: int, col: int) -> int:
            # 1. BASE CASE: WATER or OUT OF BOUNDS
            # If we try to step here, we hit a "Wall". That is +1 Perimeter.
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 1

            # 2. BASE CASE: ALREADY VISITED
            # We are on land we've seen. No new perimeter here.
            if grid[row][col] == -1:
                return 0

            # Mark as visited
            grid[row][col] = -1
            # visited.add((row, col))

            return (islandTraversal(row + 1, col) +
                    islandTraversal(row - 1, col) +
                    islandTraversal(row, col + 1) +
                    islandTraversal(row, col - 1)
                    )

        # Main Loop to find the first piece of land
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # We only have one island, so we run DFS once and return immediately
                    return islandTraversal(r, c)

        return 0