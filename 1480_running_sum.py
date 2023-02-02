from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        res = []
        for n in nums:
            res.append(n + prev)
            prev = res[-1]
        return res