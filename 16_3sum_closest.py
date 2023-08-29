from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum([*nums[:2], nums[-1]])
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            d = None
            while j < k:
                d_curr = nums[i] + nums[j] + nums[k] - target
                if d is None or abs(d_curr) < abs(d):
                    d = d_curr
                if d_curr > 0:
                    k -= 1
                elif d_curr < 0:
                    j += 1
                else:
                    return target
            if d is None:
                continue
            if abs(d) < abs(res - target):
                res = d + target
        return res
