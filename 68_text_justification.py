from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        texts = list[str]()
        while len(words) > 0:
            curr, words = self.split(words, maxWidth)
            texts.append(self.justify(curr, maxWidth, len(words) == 0))
        return texts

    def split(self, words: List[str], width: int):
        count = 0
        for i, w in enumerate(words):
            count += len(w)
            if count > width:
                return words[:i], words[i:]
            count += 1
        return words, list[str]()

    def justify(
        self,
        words: List[str],
        width: int,
        is_last: bool = False,
    ) -> str:
        n = len(words)
        if is_last or n == 1:
            res = " ".join(words)
            return res + " " * (width - len(res))
        spaces = width - sum(map(len, words))
        for i in range(1, 1 + spaces % (n - 1)):
            words[i] = " " + words[i]
        return (" " * (spaces // (n - 1))).join(words)
