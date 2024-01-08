from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        mark_live = -1
        mark_dead = 2

        def count_live(r: int, c: int):
            live = 0
            for i in range(max(0, r - 1), min(rows, r + 2)):
                for j in range(max(0, c - 1), min(cols, c + 2)):
                    if board[i][j] > 0:
                        live += 1
            return live - board[r][c]

        for r in range(rows):
            for c in range(cols):
                count = count_live(r, c)
                if board[r][c] == 0 and count == 3:
                    board[r][c] = mark_live
                elif board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = mark_dead
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == mark_live:
                    board[r][c] = 1
                elif board[r][c] == mark_dead:
                    board[r][c] = 0
