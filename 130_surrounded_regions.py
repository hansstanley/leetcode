from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m < 3 or n < 3: return
        rows, cols = {}, {}
        for r in range(1, m - 1):
            left, right = 0, n
            for c in range(0, n):
                left = c
                if board[r][c] == 'X': break
            for c in range(n - 1, left, -1):
                right = c
                if board[r][c] == 'X': break
            rows[r] = (left, right)
        for c in range(1, n - 1):
            up, down = 0, m
            for r in range(0, m):
                up = r
                if board[r][c] == 'X': break
            for r in range(m - 1, up, -1):
                down = r
                if board[r][c] == 'X': break
            cols[c] = (up, down)
        print(rows, cols)
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if (rows[r][0] <= c < rows[r][1]) and (cols[c][0] <= r < cols[c][1]):
                    board[r][c] = 'X'

board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
Solution().solve(board)
print(board)
# OXXOX
# XOOXO
# XOXOX
# OXOOO
# XXOXO

# OXXOX
# XXXXO
# XXXXX
# OXOOO
# XXOXO