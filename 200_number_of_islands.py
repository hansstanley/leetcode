from typing import List

# Attempt 2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '0': continue
                self.propagate(grid, r, c)
                count += 1
        return count
    def propagate(self, grid: List[List[str]], r: int, c: int):
        m, n = len(grid), len(grid[0])
        if r < 0 or r >= m: return
        if c < 0 or c >= n: return
        if grid[r][c] != '1': return

        grid[r][c] = '0'
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            self.propagate(grid, r + dr, c + dc)

# Attempt 1
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid: return count
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    self.propagate(grid, r, c)
        return count
    def propagate(self, grid: List[List[str]], r: int, c: int) -> None:
        if r < 0 or r >= len(grid): return
        if c < 0 or c >= len(grid[0]): return
        if grid[r][c] != '1': return
        grid[r][c] = None
        self.propagate(grid, r - 1, c)
        self.propagate(grid, r + 1, c)
        self.propagate(grid, r, c - 1)
        self.propagate(grid, r, c + 1)