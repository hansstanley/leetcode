class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        first_c = s[0]
        i = s.find(first_c, 1)
        while i != -1:
            if i > len(s) // 2: return False
            if s == s[i:] + s[:i]: return True
            i = s.find(first_c, i + 1)
        return False

sol = Solution()
for s in ['a', 'aba', 'abab', 'abcabcabc', 'aabaaba']:
    print(sol.repeatedSubstringPattern(s))