from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        sums = []
        prev_a = None
        for i, a in enumerate(nums):
            if a == prev_a: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                sum = a + b + c
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    sums.append([a, b, c])
                    while l < r and nums[l] == b: l += 1
                    while l < r and nums[r] == c: r -= 1
            prev_a = a
        return sums
        
print(Solution().threeSum([0,0,0]))