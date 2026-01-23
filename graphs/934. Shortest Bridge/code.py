from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Use DFS to find coordinate of an island, and BFS to find shortest path to connect
        # nxn matrix. so #rows = #columns
        N = len(grid)

        # all 4 directions
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),  # Horizontal/Vertical
        ]

        # At each neighbour we keep track of the distance till that neighbour
        # [row, col, flips]. flips = how many 0's had to be flipped
        island_1_map = deque()

        """
        Phase 1: Use DFS to find the coordinate of an island and changed their
        1's to 2's to mark as visited.
        This will help later in the sense that, when we will find a 1, we know
        it would be the other island
        """

        def dfs_island_searcher(r, c):
            if r < 0 or r >= N or c < 0 or c >= N or grid[r][c] != 1:
                return

            island_1_map.append((r, c))
            grid[r][c] = 2

            for dr, dc in directions:
                dfs_island_searcher(r + dr, c + dc)

        # Main loops
        found = False
        for r in range(N):
            if found: break
            for c in range(N):
                if grid[r][c] == 1:
                    # find the rest of the island
                    found = True
                    dfs_island_searcher(r, c)
                    break

        # Phase 2: BFS to find shortest connecting bridge
        distance = 0
        while island_1_map:

            # iteration for 1 level at a time (current num of cells in island_1_map)
            # each level we traverse = distance of 1
            for _ in range(len(island_1_map)):
                r, c = island_1_map.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Bounds check
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == 1:
                            return distance

                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            island_1_map.append((nr, nc))

            # increment by 1 after processing the whole layer
            distance += 1

        return -1






