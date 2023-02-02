from typing import List

<too slow>
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        if len(nums) < 2: return max_sum
        sums = {}
        for i in range(len(nums)):
            sums[(i, i + 1)] = nums[i]
        for i in range(2, len(nums) + 1):
            next_sums = {}
            for j in range(0, len(nums) - i + 1):
                s = next_sums[(j, j + i)] = sums[(j, j + i - 1)] + nums[j + i - 1]
                max_sum = max(max_sum, s)
            sums = next_sums
        return max_sum
    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_sum = max(nums)
    #     if len(nums) < 2: return max_sum
    #     sums = {}
    #     for i in range(len(nums)):
    #         sums[(i, i + 1)] = nums[i]
    #     for i in range(2, len(nums) + 1):
    #         mid = i // 2
    #         for j in range(0, len(nums) - i + 1):
    #             s = sums[(j, j + i)] = sums[(j, j + mid)] + sums[(j + mid, j + i)]
    #             max_sum = max(max_sum, s)
    #     return max_sum

print(Solution().maxSubArray([8]))