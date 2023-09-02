from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        l_idx = self.b_search([i[1] for i in intervals], newInterval[0])
        r_idx = self.b_search([i[0] for i in intervals], newInterval[1], 1)
        return [
            *intervals[:l_idx],
            self.merge(intervals[l_idx:r_idx], newInterval),
            *intervals[r_idx:],
        ]

    def b_search(self, nums: List[int], x: int, delta: int = 0) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] == x:
                return m + delta
            if nums[m] < x:
                lo = m + 1
            else:
                hi = m
        return lo

    def merge(self, intervals: List[List[int]], newInterval: List[int]) -> List[int]:
        if len(intervals) == 0:
            return newInterval
        return [
            min(intervals[0][0], newInterval[0]),
            max(intervals[-1][1], newInterval[1]),
        ]


print("ans", Solution().insert([[1, 5]], [2, 3]))
print("ans", Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print("ans", Solution().insert([[1, 3], [6, 9]], [2, 5]))
