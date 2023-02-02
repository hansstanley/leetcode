from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            l_peak = m == 0 or nums[m] > nums[m - 1]
            r_peak = m == len(nums) - 1 or nums[m] > nums[m + 1]
            if l_peak and r_peak: return m
            if l_peak: l = m + 1
            if r_peak: r = m
        