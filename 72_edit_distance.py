from typing import Dict, Tuple


class Solution:
    delta: Dict[Tuple[str, str], int] = {}

    def minDistance(self, word1: str, word2: str, origin: bool = True) -> int:
        if origin:
            self.delta.clear()
        if (word1, word2) in self.delta:
            return self.delta[(word1, word2)]
        l1, l2 = len(word1), len(word2)
        if 0 in {l1, l2}:
            return max(l1, l2)
        tail1, tail2 = word1[1:], word2[1:]
        ops: int
        if word1[0] == word2[0]:
            ops = self.minDistance(tail1, tail2, False)
        else:
            ops = 1 + min(
                self.minDistance(tail1, word2, False),
                self.minDistance(word1, tail2, False),
                self.minDistance(tail1, tail2, False),
            )
        self.delta[(word1, word2)] = ops
        return ops
