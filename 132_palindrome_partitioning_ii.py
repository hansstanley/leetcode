class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        mat = [[r == c for c in range(n)] for r in range(n)]
        for r in range(n - 2, -1, -1):
            for c in range(r + 1, n):
                mat[r][c] = s[r] == s[c]
                if c - r > 1:
                    mat[r][c] = mat[r][c] and mat[r + 1][c - 1]

        cut = [n - 1] * n
        cut.append(-1)
        for r in range(n - 1, -1, -1):
            for c in range(r, n):
                if mat[r][c]:
                    cut[r] = min(cut[r], cut[c + 1] + 1)
        return cut[0]


print(Solution().minCut("aaabaa"))
