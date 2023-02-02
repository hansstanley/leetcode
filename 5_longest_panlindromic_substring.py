class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        matrix = [[i == j for j in range(n)] for i in range(n)]
        longest = s[0]
        for r in range(n - 2, -1, -1):
            for c in range(r + 1, n):
                if c - r == 1:
                    matrix[r][c] = s[r] == s[c]
                else:
                    matrix[r][c] = s[r] == s[c] and matrix[r + 1][c - 1]
                if matrix[r][c] and c - r + 1 > len(longest):
                    longest = s[r:c + 1]
        return longest


print(Solution().longestPalindrome("cbbd"))
