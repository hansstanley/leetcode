from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff = [r - l for l, r in zip(nums[:-1], nums[1:])]
        return all([d >= 0 for d in diff]) or all([d <= 0 for d in diff])

print(Solution().isMonotonic([1, 2, 3, 2]))