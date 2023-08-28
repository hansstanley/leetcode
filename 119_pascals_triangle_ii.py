from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res: List[int] = [1]
        lo, hi = 1, rowIndex
        for _ in range(rowIndex // 2):
            res.append(round(res[-1] * (hi / lo)))
            hi -= 1
            lo += 1
        if rowIndex % 2 == 0:
            return res + res[::-1][1:]
        return res + res[::-1]
