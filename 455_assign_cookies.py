from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        while len(s) > 0:
            curr_s = s.pop()
            while len(g) > 0:
                curr_g = g.pop()
                if curr_s >= curr_g:
                    count += 1
                    break
        return count