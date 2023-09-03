from typing import Dict, List, Tuple


class Solution:
    combinations: Dict[Tuple[int, int, int], List[List[int]]] = {}

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations.clear()
        return self.helper(k, 1, n + 1)

    def helper(self, k: int, lo: int, hi: int) -> List[List[int]]:
        if (lo, hi) in self.combinations:
            return self.combinations[(k, lo, hi)]
        res: List[List[int]] = []
        if hi - lo < k:
            res = []
        elif hi - lo == k:
            res = [list(range(lo, hi))]
        elif k == 1:
            res = [[i] for i in range(lo, hi)]
        else:
            res.extend([[lo, *c] for c in self.helper(k - 1, lo + 1, hi)])
            res.extend(self.helper(k, lo + 1, hi))
        self.combinations[(k, lo, hi)] = res
        return res
