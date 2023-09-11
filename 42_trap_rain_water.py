from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        rain, n = 0, len(height)
        if n < 3:
            return 0
        l_height: List[int] = [height[0]] + [0] * (n - 1)
        r_height: List[int] = [0] * (n - 1) + [height[n - 1]]
        for idx in range(1, n):
            l_height[idx] = max(l_height[idx - 1], height[idx])
        for idx in range(n - 2, -1, -1):
            r_height[idx] = max(r_height[idx + 1], height[idx])
        for idx in range(0, n):
            rain += min(l_height[idx], r_height[idx]) - height[idx]
        return rain
