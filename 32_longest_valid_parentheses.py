class Solution:
    def longestValidParentheses(self, s: str) -> int:
        indices = [-1]
        for i, p in enumerate(s):
            if p == "(":
                indices.append(i)
                continue
            if indices[-1] == -1 or s[indices[-1]] == ")":
                indices.append(i)
                continue
            indices.pop()
        indices.append(len(s))
        m = 0
        for i, j in zip(indices[:-1], indices[1:]):
            m = max(m, j - i - 1)
        return m


print(Solution().longestValidParentheses(")()(((())))("))
