from typing import List, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        low1, profit1 = prices[0], 0
        low2, profit2 = prices[0], 0
        for p in prices:
            low1 = min(low1, p)
            profit1 = max(profit1, p - low1)
            low2 = min(low2, p - profit1)
            profit2 = max(profit2, p - low2)
        return profit2


class Solution1_Failed:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, profit1 = self.findMinMax(prices, 0, len(prices))
        if buy1 == -1 or sell1 == -1 or profit1 == 0:
            return 0
        _, _, profit2 = self.findMinMax(prices, 0, buy1)
        _, _, profit3 = self.findMinMax(prices, sell1, len(prices))
        return profit1 + max(profit2, profit3)

    def findMinMax(
        self, prices: List[int], idx_min: int, idx_max: int
    ) -> Tuple[int, int, int]:
        if not prices:
            return -1, -1, 0
        low, profit = prices[idx_min], 0
        idx_sell = -1
        for i in range(idx_min, idx_max):
            p = prices[i]
            low = min(low, p)
            if p - low > profit:
                idx_sell = i
                profit = p - low
        if idx_sell == -1:
            return -1, -1, 0
        low = prices[idx_sell] - profit
        idx_buy = idx_sell
        while prices[idx_buy] != low:
            idx_buy -= 1
        return idx_buy, idx_sell, profit


print(Solution().maxProfit([3, 2, 1]))
