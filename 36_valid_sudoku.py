from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid_list(row):
                return False
        for c in range(9):
            col = [row[c] for row in board]
            if not self.is_valid_list(col):
                return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = []
                for k in range(r, r + 3):
                    box.extend(board[k][c : c + 3])
                if not self.is_valid_list(box):
                    return False
        return True

    def is_valid_list(self, nums: List[str]) -> bool:
        seen = set()
        for n in nums:
            if n == ".":
                continue
            if n in seen:
                return False
            seen.add(n)
        return True
