from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.strMatch(s, pattern) for s in queries]
    def strMatch(self, s: str, pattern: str) -> bool:
        i = 0
        for c in s:
            if c.isupper():
                if i >= len(pattern) or c != pattern[i]: return False
                i += 1
            else:
                if i < len(pattern) and c == pattern[i]: i += 1
        return i == len(pattern)