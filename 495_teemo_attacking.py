from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        seconds = duration
        for i in range(len(timeSeries) - 1):
            seconds += min(duration, timeSeries[i + 1] - timeSeries[i])
        return seconds
