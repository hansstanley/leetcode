class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def next_moves(j1: int, j2: int):
            return [(jug1Capacity, j2), (0, j2),
                    (j1, jug2Capacity), (j1, 0),
                    (min(jug1Capacity, j1 + j2), max(0, j2 - (jug1Capacity - j1))),
                    (max(0, j1 - (jug2Capacity - j2)), min(jug2Capacity, j1 + j2))]
        memo = set()
        stack = [(0, 0)]
        while len(stack) > 0:
            j1, j2 = stack.pop()
            if (j1, j2) in memo: continue
            if j1 + j2 == targetCapacity: return True
            memo.add((j1, j2))
            stack.extend(next_moves(j1, j2))
        return False

print(Solution().canMeasureWater(3, 5, 4))