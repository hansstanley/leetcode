from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            else:
                l = m
        return l if nums[l] == target else -1

print(Solution().search([-1,0,3,5,9,12], -1))