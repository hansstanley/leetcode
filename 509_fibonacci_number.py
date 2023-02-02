class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        prev, curr, i = 1, 1, 2
        while i < n:
            prev, curr = curr, prev + curr
            i += 1
        return curr