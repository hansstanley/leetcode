from typing import Dict, List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        memo = {}
        return max(
            self.choose(nums, 1, {}),
            self.choose(nums[:-1], 0, {})
        )
    def choose(self, nums: List[int], h: int, memo = Dict) -> int:
        if h >= len(nums): return 0
        if memo.get(h) is not None: return memo[h]
        memo[h] = max(
            self.choose(nums, h + 2, memo) + nums[h],
            self.choose(nums, h + 1, memo)
        )
        return memo[h]

print(Solution().rob([200,3,140,20,10]))