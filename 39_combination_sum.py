from typing import Dict, List


class Solution:
    memo: Dict[int, int] = {}
    sums: List[List[int]] = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sums.clear()
        self.dfs(candidates, target, [])
        return self.sums
    def dfs(self, candidates: List[int], target: int, comb: List[int]):
        if target < 0: return
        if target == 0:
            self.sums.append(comb)
            return
        for i, c in enumerate(candidates):
            next_comb = comb.copy()
            next_comb.append(c)
            self.dfs(candidates[i:], target - c, next_comb)