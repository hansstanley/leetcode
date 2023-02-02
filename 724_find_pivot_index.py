from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        l_sum = 0
        for i, n in enumerate(nums):
            if l_sum == (s - n) / 2: return i
            l_sum += n
        return -1