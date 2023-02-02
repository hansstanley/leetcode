from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        intersect = []
        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i], secondList[j]
            l, r = max(a[0], b[0]), min(a[1], b[1])
            if l <= r: intersect.append([l, r])
            if a[1] < max(a[1], b[1]):
                i += 1
            elif b[1] < max(a[1], b[1]):
                j += 1
            else:
                i += 1
                j += 1
        return intersect