from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        code = [0]
        diff = 1
        for _ in range(n):
            for i in range(len(code) - 1, -1, -1):
                code.append(code[i] + diff)
            diff <<= 1
        return code
