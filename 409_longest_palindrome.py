class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for c in s:
            letters.setdefault(c, 0)
            letters[c] += 1
        count = 0
        has_odd = False
        for i in letters.values():
            count += i // 2 * 2
            if i % 2 == 1: has_odd = True
        return count + (1 if has_odd else 0)

Solution().longestPalindrome('hello')