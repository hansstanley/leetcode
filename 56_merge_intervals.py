from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in intervals:
            if merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
        return merged

# Attempt 1
class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        curr = None
        intervals.sort()
        for i in range(0, len(intervals)):
            if not curr: curr = intervals[i]
            if intervals[i][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[i][1])
            else:
                res.append(curr)
                curr = intervals[i]
        res.append(curr)
        return res