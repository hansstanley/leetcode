from typing import Dict, List, Tuple


class Solution:
    visited: Dict[Tuple[int, int], int] = {}

    def minimumTotal(
        self,
        triangle: List[List[int]],
        r: int = 0,
        c: int = 0,
    ) -> int:
        if r == c == 0:
            self.visited = {}
        rows = len(triangle)
        if r == rows - 1:
            return triangle[r][c]
        if (r, c) not in self.visited:
            left = self.minimumTotal(triangle, r + 1, c)
            right = self.minimumTotal(triangle, r + 1, c + 1)
            self.visited[(r, c)] = min(left, right) + triangle[r][c]
        return self.visited[(r, c)]
