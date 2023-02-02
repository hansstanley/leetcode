from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] < target: i += 1
            elif nums[j] > target: j -= 1
            else: break
        return [i, j] if i <= j else [-1, -1]
        return [self.binarySearch(nums, target), self.reversedBinarySearch(nums, target)]
    def binarySearch(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        l, r = 0, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m
        return l if nums[l] == target else -1
    def reversedBinarySearch(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        l, r = -1, len(nums) - 1
        while r - l > 1:
            m = (l + r + 2) // 2 + ((l + r + 2) % 2) - 1
            if nums[m] < target:
                r = m
            else:
                l = m
        return r if nums[r] == target else -1

print(Solution().searchRange([1], 1))