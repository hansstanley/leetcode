class Solution:
    def tribonacci(self, n: int) -> int:
        i, t = 2, [0, 1, 1]
        if n < 3: return t[n]
        while i < n:
            t[0], t[1], t[2] = t[1], t[2], t[0] + t[1] + t[2]
            i += 1
        return t[2]