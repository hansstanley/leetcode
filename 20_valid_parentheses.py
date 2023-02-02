class Solution:
    def isValid(self, s: str) -> bool:
        p, m = [], {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in '([{':
                p.append(c)
            elif len(p) > 0 and p[-1] == m[c]:
                p.pop()
            else:
                return False
        return len(p) == 0

print(Solution().isValid('([{]})'))