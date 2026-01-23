from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotting_queue = deque()
        numFreshOranges = 0
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # get the location of rotting oranges
        # get the number of Fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotting_queue.append((r, c))

                elif grid[r][c] == 1:
                    numFreshOranges += 1

        if numFreshOranges == 0:
            return 0

        # numFresh > 0 because if it was >= 0, at = 0, there isn't anything no more to infect
        while rotting_queue and numFreshOranges > 0:
            minutes += 1

            """
            This for loop simulates a minutes timeframe
            
            Freeze! How many items are in the queue right now? Okay, 5 items. 
            These 5 items represent Minute 1. I will process exactly these 5 items. 
            Any new items discovered (Minute 2 items) will be added to the back, 
            but I won't touch them until this loop finishes.
            """
            for _ in range(len(rotting_queue)):
                r, c = rotting_queue.popleft()

                for dr, dc in neighbours:
                    row, col = r + dr, c + dc

                    # infect the fresh orange
                    if (0 <= row < rows) and (0 <= col < cols) and grid[row][col] == 1:
                            grid[row][col] = 2
                            numFreshOranges -= 1
                            # add the new infected oranges to the queue
                            # spreading out...
                            rotting_queue.append((row, col))

        return minutes if  numFreshOranges == 0 else -1









