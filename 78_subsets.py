from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helper(nums)

    def helper(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        others = self.helper(nums[1:])
        others.extend([[nums[0], *s] for s in others])
        return others
