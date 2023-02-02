from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [g - c for g, c in zip(gas, cost)]
        if sum(delta) < 0: return -1
        n = len(delta)
        delta *= 2
        for i in range(n):
            if sum(delta[i:i+n]) >= 0: return i
        return -1
