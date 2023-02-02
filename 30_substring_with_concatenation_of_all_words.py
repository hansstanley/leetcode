from typing import List, Set

<unsolved>
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words)
        m = len(words[0])
        n = len(s)
        if len(words) == 0: return []
        if n < m * k: return []

        words_all: Set[str] = {}
        words_left: Set[str] = {}
        for word in words:
            words_all.add(word)
            words_left.add(word)
        for i, j in zip(range(0, n - m * k, m))