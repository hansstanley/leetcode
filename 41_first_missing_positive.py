from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] if 0 < nums[i] < n else 0
        for i in range(n):
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] < n:
                return i
        return n


print(Solution().firstMissingPositive([2, 2]))
