import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = re.sub(r"[^a-zA-Z0-9]+", "", s).lower()
        n = len(parsed) // 2
        return parsed[:n] == parsed[::-1][:n]
