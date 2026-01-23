from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Use BFS, level traversal
        # Principle: Like ripples on water, traverse neighbours level by level
        # The first neighbour to reach target location, wins. returns its length travelled

        # nxn matrix. so #rows = #columns
        N = len(grid)

        # if N-1, N-1 is a wall (=1), then no shortest path exists
        if grid[N - 1][N - 1] == 1 or grid[0][0] == 1:
            return -1

        # All 8 directions
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),  # Horizontal/Vertical
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonals
        ]

        # At each neighbour we keep track of the distance till that neighbour
        # [row, col, distance]. distance = # cells visited. so (0, 0) counts as 1
        neighbours = deque([(0, 0, 1)])

        while neighbours:
            # get the row, col and length of the next cell to visit
            r, c, length = neighbours.popleft()

            # Win?
            if r == N - 1 and c == N - 1:
                return length

            # look at its valid neighbours. new row, new col
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # check if new row and col doesn't lead us out of bounds
                # and is a valid neighbout
                if (0 <= nr < N) and (0 <= nc < N) and grid[nr][nc] == 0:
                    # since we're at the cell, mark it as visited
                    grid[nr][nc] = 1

                    # append the cell to the queue (neighbours), so we'll check its neighbours later
                    neighbours.append((nr, nc, length + 1))

        return -1



