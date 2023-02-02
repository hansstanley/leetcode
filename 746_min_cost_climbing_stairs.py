from typing import Dict, List, Set


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.stepper(cost, 0, memo), self.stepper(cost, 1, memo))
    def stepper(self, cost: List[int], step: int, memo: Dict) -> int:
        if step >= len(cost) - 2: return cost[step]
        if memo.get(step) is not None: return memo[step]
        c1 = self.stepper(cost, step + 1, memo)
        c2 = self.stepper(cost, step + 2, memo)
        memo[step] = cost[step] + min(c1, c2)
        return memo[step]