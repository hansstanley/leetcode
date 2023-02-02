from typing import Dict, List


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.choose(nums, 0, memo)
    def choose(self, nums: List[int], h: int, memo: Dict) -> int:
        if h >= len(nums): return 0
        if memo.get(h) is not None: return memo[h]
        memo[h] = max(
            nums[h] + self.choose(nums, h + 2, memo),
            self.choose(nums, h + 1, memo)
        )
        return memo[h]