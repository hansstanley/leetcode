from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _, _, max_profit = self.traverse(prices, 0, len(prices))
        return max_profit
    
    def traverse(self, prices: List[int], l: int, r: int):
        if r - l == 1: return prices[l], prices[l], 0
        m = (l + r) // 2
        l_min, l_max, l_val = self.traverse(prices, l, m)
        r_min, r_max, r_val = self.traverse(prices, m, r)
        return min(l_min, r_min), max(l_max, r_max), max(l_val, r_val, r_max - l_min)

print(Solution().maxProfit([7,6,4,3,1]))