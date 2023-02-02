from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        return nums[r % len(nums)]