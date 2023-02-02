from typing import Dict, List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts.setdefault(n, 0)
            counts[n] += 1
        houses = [0] * max(counts.keys())
        for n, i in counts.items():
            houses[n - 1] = n * i
        return self.rob(houses, 0, {})
    def rob(self, houses: List[int], h: int, memo: Dict) -> int:
        if h >= len(houses): return 0
        if memo.get(h) is not None: return memo[h]
        memo[h] = max(
            self.rob(houses, h + 1, memo),
            self.rob(houses, h + 2, memo) + houses[h]
        )
        return memo[h]