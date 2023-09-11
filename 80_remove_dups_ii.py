from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        last, quota = None, 1
        i = j = 0
        while i <= j < n:
            if quota == 0:
                while j < n and nums[j] == last:
                    j += 1
                if j == n:
                    break
            quota = quota - 1 if nums[j] == last else 1
            last = nums[j]
            nums[i] = nums[j]
            i += 1
            j += 1
        return i


nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums), nums)
