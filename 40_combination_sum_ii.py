from typing import List, Set, Tuple


class Solution:
    def combinationSum2(
        self,
        candidates: List[int],
        target: int,
    ) -> List[List[int]]:
        candidates.sort()
        res = self.find([], 0, candidates, target)
        return [list(c) for c in res]

    def find(
        self,
        combi: List[int],
        combi_sum: int,
        candidates: List[int],
        target: int,
    ) -> Set[Tuple[int]]:
        if combi_sum == target:
            return {tuple(combi)}
        if combi_sum > target or len(candidates) == 0:
            return set()
        take = self.find(
            [*combi, candidates[0]],
            combi_sum + candidates[0],
            candidates[1:],
            target,
        )
        take_not = self.find(
            combi,
            combi_sum,
            [c for c in candidates if c != candidates[0]],
            target,
        )
        return take.union(take_not)
