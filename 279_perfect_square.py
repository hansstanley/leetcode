from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i ** 2 <= n:
            squares.append(i ** 2)
            i += 1
        squares.reverse()
        # print(squares)
        return self.traverse(n, squares, squares[0])
    def traverse(self, n: int, squares: List[int], largest: int, memo = {}):
        if n < 0: return -1
        if n == 0: return 0
        if memo.get(n) is not None: return memo[n]
        counts = []
        for sq in squares:
            if sq > largest: continue
            count = self.traverse(n - sq, squares, sq)
            if count >= 0: counts.append(count + 1)
        memo[n] = min(counts)
        # print(n, memo[n])
        return memo[n]
            
print(Solution().numSquares(9))