class Solution:
    def numSquares(self, n: int) -> int:
        mem = [n] * (n + 1)
        mem[0] = 0
        x = 1
        while x**2 <= n:
            x_sq = x**2
            for i in range(x_sq, n + 1):
                mem[i] = min(mem[i], mem[i - x_sq] + 1)
            x += 1
        return mem[n]


print(Solution().numSquares(10))
