from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if n < k or k == 0: return []
        letters = {}
        for c in p: letters[c] = letters.get(c, 0) + 1
        res = []
        for i in range(n):
            letters[s[i]] = letters.get(s[i], 0) - 1
            if i - k >= 0:
                letters[s[i - k]] = letters.get(s[i - k], 0) + 1
            if all([i == 0 for i in letters.values()]): res.append(i - k + 1)
        return res

print(Solution().findAnagrams('cbaebabacd', 'abc'))