from typing import Dict, List, Tuple


class Solution1:
    walked: Dict[Tuple[int, int], int] = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.walked.clear()
        return self.walker(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))

    def walker(
        self,
        grid: List[List[int]],
        curr: Tuple[int, int],
        goal: Tuple[int, int],
    ) -> int:
        if curr in self.walked:
            return self.walked[curr]
        if curr == goal:
            return grid[goal[0]][goal[1]]

        next_scores: List[int] = []
        if curr[0] < len(grid) - 1:
            next_scores.append(self.walker(grid, (curr[0] + 1, curr[1]), goal))
        if curr[1] < len(grid[0]) - 1:
            next_scores.append(self.walker(grid, (curr[0], curr[1] + 1), goal))
        self.walked[curr] = grid[curr[0]][curr[1]] + min(next_scores)
        return self.walked[curr]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        cost: List[List[int]] = [[0 for _ in range(c)] for _ in range(r)]
        cost[-1][-1] = grid[-1][-1]
        for i in range(r - 2, -1, -1):
            cost[i][-1] = cost[i + 1][-1] + grid[i][-1]
        for j in range(c - 2, -1, -1):
            cost[-1][j] = cost[-1][j + 1] + grid[-1][j]
        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                cost[i][j] = min(cost[i + 1][j], cost[i][j + 1]) + grid[i][j]
        return cost[0][0]


sol = Solution()
print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
