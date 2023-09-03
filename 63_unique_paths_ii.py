from typing import Dict, List, Tuple


class Solution:
    walked: Dict[Tuple[int, int], int] = {}

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.walked.clear()
        return self.walker(
            obstacleGrid,
            (0, 0),
            (len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1),
        )

    def walker(
        self,
        grid: List[List[int]],
        curr: Tuple[int, int],
        goal: Tuple[int, int],
    ) -> int:
        if curr in self.walked:
            return self.walked[curr]
        if grid[curr[0]][curr[1]] == 1:
            return 0
        if curr == goal:
            return 1
        r_score = (
            0
            if curr[1] == len(grid[0]) - 1
            else self.walker(grid, (curr[0], curr[1] + 1), goal)
        )
        d_score = (
            0
            if curr[0] == len(grid) - 1
            else self.walker(grid, (curr[0] + 1, curr[1]), goal)
        )
        self.walked[curr] = r_score + d_score
        return self.walked[curr]


sol = Solution()
print(sol.uniquePathsWithObstacles([[0, 1], [0, 0]]))
print(sol.walked)
