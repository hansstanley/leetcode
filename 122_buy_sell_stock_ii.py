from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        profit = 0
        for i, j in zip(prices[:-1], prices[1:]):
            profit += max(0, j - i)
        return profit