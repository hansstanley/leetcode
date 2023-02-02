from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for w1 in words:
            for w2 in words:
                if w1 in w2 and w1 != w2:
                    res.append(w1)
                    break
        return  res

print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))