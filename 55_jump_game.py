from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_count = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= zero_count:
                zero_count += 1
            else:
                zero_count = 0
        return zero_count == 0

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))