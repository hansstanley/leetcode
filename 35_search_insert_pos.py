from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while hi - lo > 1:
            m = (lo + hi) // 2
            if nums[m] < target:
                lo = m
            elif nums[m] > target:
                hi = m
            else:
                return m
        if nums[lo] >= target:
            return lo
        return hi
