class Solution:
    def mySqrt(self, x: int) -> int:
        return self.helper(x, 0, x)
    def helper(self, x: int, a: int, b: int) -> int:
        if a * a == x: return a
        if b * b == x: return b
        if b - a <= 1: return a
        c = a + (b - a) // 2
        if c * c <= x:
            return self.helper(x, c, b)
        else:
            return self.helper(x, a, c)