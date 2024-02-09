from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        fuel = 0
        start = 0
        for i in range(n):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                fuel = 0
                start = i + 1
        if start == n:
            return -1
        for i in range(start):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                return -1
        return start
