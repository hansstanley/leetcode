from typing import List, Optional


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap: Optional[int] = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                swap = i - 1
                break
        if swap is None:
            nums.reverse()
            return
        swap_with = swap + 1
        for i in range(swap + 1, len(nums)):
            if nums[swap] < nums[i] <= nums[swap_with]:
                swap_with = i
            else:
                break
        nums[swap], nums[swap_with] = nums[swap_with], nums[swap]

        i, j = swap + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
