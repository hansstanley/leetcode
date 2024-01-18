from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        mat = [[r == c for c in range(n)] for r in range(n)]
        for r in range(n - 2, -1, -1):
            for c in range(r + 1, n):
                mat[r][c] = s[r] == s[c]
                if c - r > 1:
                    mat[r][c] = mat[r][c] and mat[r + 1][c - 1]

        def find_partitions(r: int) -> List[List[str]]:
            if r >= n:
                return [[]]
            if r == n - 1:
                return [[s[r]]]
            parts = find_partitions(r + 1)
            for i in range(len(parts)):
                parts[i].insert(0, s[r])
            for c in range(r + 1, n):
                if mat[r][c]:
                    partials = find_partitions(c + 1)
                    for p in partials:
                        parts.append([s[r : c + 1], *p])
            return parts

        return find_partitions(0)


print(Solution().partition("baaabcba"))
