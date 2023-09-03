from typing import List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    continue
                self.splash(matrix, r, c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = matrix[r][c] or 0

    def splash(self, matrix: List[List[Optional[int]]], r: int, c: int):
        for j in range(len(matrix[0])):
            matrix[r][j] = matrix[r][j] and None
        for i in range(len(matrix)):
            matrix[i][c] = matrix[i][c] and None
