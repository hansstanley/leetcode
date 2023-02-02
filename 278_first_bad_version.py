# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool: return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1): return 1
        l, r = 1, n
        while r - l > 1:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r