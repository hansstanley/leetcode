from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res: List[List[int]] = [[1]]
        for _ in range(numRows - 1):
            row: List[int] = []
            for i, j in zip([0, *res[-1]], [*res[-1], 0]):
                row.append(i + j)
            res.append(row)
        return res
