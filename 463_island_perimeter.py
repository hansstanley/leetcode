from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                if r - 1 < 0 or grid[r - 1][c] == 0: count += 1
                if r + 1 >= m or grid[r + 1][c] == 0: count += 1
                if c - 1 < 0 or grid[r][c - 1] == 0: count += 1
                if c + 1 >= n or grid[r][c + 1] == 0: count += 1
        return count

print(Solution().islandPerimeter([[1, 0]]))