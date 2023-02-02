from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = self.find_rotation(nums)
        l, r = 0, len(nums)
        if target <= nums[-1]:
            l = start
        elif target >= nums[0]:
            r = end
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m
        return l if nums[l] == target else -1
    def find_rotation(self, nums: List[int]):
        l, r = 0, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        return r % len(nums), l + 1

print(Solution().search([3, 4, 1, 2], 4))