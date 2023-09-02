from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.fill(matrix, 0, n - 1, 1)
        return matrix

    def fill(self, matrix: List[List[int]], lo: int, hi: int, start: int):
        if lo > hi:
            return
        if lo == hi:
            matrix[lo][hi] = start
            return
        for i in range(lo, hi):
            matrix[lo][i] = start
            start += 1
        for i in range(lo, hi):
            matrix[i][hi] = start
            start += 1
        for i in range(hi, lo, -1):
            matrix[hi][i] = start
            start += 1
        for i in range(hi, lo, -1):
            matrix[i][lo] = start
            start += 1
        self.fill(matrix, lo + 1, hi - 1, start)


print(Solution().generateMatrix(3))
