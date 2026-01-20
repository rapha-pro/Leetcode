from typing import List, Set, Tuple

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid[0]), len(grid[0][0])
        visited: Set[Tuple[int, int]] = set()
        num_islands = 0

        # helper function (The "Sinking" logic)
        def islandSinker_dfs(row: int, col: int):
            # 1. Base case: Check bounds and if it is water
            # If r or c are outside the grid OR it is '0' (water/visited), stop.
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0' or (row, col) in visited:
                return

            # 2. Sink the island/ Mark as visited
            visited.add((row, col))

            # 3. Visit Neighbours (Down, Up, Right, Left)
            islandSinker_dfs(row - 1, col)
            islandSinker_dfs(row + 1, col)
            islandSinker_dfs(row, col - 1)
            islandSinker_dfs(row, col + 1)


        # Main loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    num_islands += 1

                    islandSinker_dfs(r, c)

        return num_islands