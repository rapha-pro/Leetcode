from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # using DFS
        rows, cols = len(image), len(image[0])
        color_of_source = image[sr][sc]

        def neighbour_flood_filler(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or image[row][col] == color:
                return

            # only can paint if current pixel matches color of source pixel
            if image[row][col] != color_of_source:
                return

            image[row][col] = color

            neighbour_flood_filler(row + 1, col)
            neighbour_flood_filler(row - 1, col)
            neighbour_flood_filler(row, col + 1)
            neighbour_flood_filler(row, col - 1)

        neighbour_flood_filler(sr, sc)

        return image


