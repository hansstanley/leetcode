from typing import List

<unsolved>
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        frontier, level = [beginWord], 0
        while len(frontier) > 0:
            print(list(words))
            level += 1
            for word in frontier:
                if word == endWord: return level
            next_frontier = [w for w in words if self.is_next(frontier, w)]
            for w in next_frontier: words.discard(w)
            frontier = next_frontier
        return 0

    def is_next(self, words: List[str], next_word: str) -> bool:
        for w in words:
            if self.is_adj(w, next_word): return True
        return False

    def is_adj(self, curr_word: str, next_word: str) -> bool:
        count = 0
        for i, j in zip(curr_word, next_word):
            if i == j: continue
            if count: return False
            count += 1
        return True

Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])