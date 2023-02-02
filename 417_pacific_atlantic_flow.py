from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        memo = {}

    def dfs(self, heights: List[List[int]], r: int, c: int, memo = {}):
        if memo.get()