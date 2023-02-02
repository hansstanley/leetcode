class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        a, b = m + n - 2, min(m, n) - 1
        return self.factorial(a, a - b) // self.factorial(b, 0)
    def factorial(self, x_from: int, x_to: int) -> int:
        prod = 1
        while x_from > x_to:
            prod *= x_from
            x_from -= 1
        return prod