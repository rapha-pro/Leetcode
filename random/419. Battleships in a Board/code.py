from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    if (r - 1 >= 0 and board[r - 1][c] == "X") or (board[r][c - 1] == "X" and c - 1 >= 0):
                        pass
                    else:
                        count += 1

        return count