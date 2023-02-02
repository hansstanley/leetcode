class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        # Attempt 2
        i = len(haystack.split(needle)[0])
        return -1 if len(haystack) == i else i
        # Attempt 1
        try:
            return haystack.index(needle)
        except ValueError:
            return -1