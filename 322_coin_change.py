from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        inf = amount + 1
        mem = dict[tuple[int, int], int]()

        def dp(i: int, remaining: int):
            k = (i, remaining)
            if k in mem:
                return mem[k]
            if i >= len(coins):
                return inf
            if remaining < 0:
                return inf
            if remaining == 0:
                return 0
            take = 1 + dp(i, remaining - coins[i])
            drop = dp(i + 1, remaining)
            mem[k] = min(take, drop)
            return mem[k]

        res = dp(0, amount)
        return res if res < inf else -1


print(Solution().coinChange([3, 7, 405, 436], 8839))
