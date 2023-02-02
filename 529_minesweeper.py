from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        elif board[r][c] == 'E':
            next_clicks = self.neighbours(board, r, c)
            mine_count = sum([board[i][j] == 'M' for (i, j) in next_clicks])
            if mine_count == 0:
                board[r][c] = 'B'
                for (i, j) in next_clicks: self.updateBoard(board, [i, j])
            else:
                board[r][c] = str(mine_count)
        return board
    def neighbours(self, board: List[List[str]], r: int, c: int):
        res = []
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): continue
                if i == r and j == c: continue
                res.append((i, j))
        return res