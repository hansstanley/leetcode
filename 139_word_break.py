from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0: return False
        res = False
        for word in wordDict:
            if word in s:
                if len(word) == len(s): return True
                next_s = s.split(word)
                res = res or any([self.wordBreak(n_s, wordDict) for n_s in next_s])
        return res