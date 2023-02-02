from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_i = 0
        for color in range(3):
            for i in range(curr_i, len(nums)):
                if nums[i] == color:
                    nums[i], nums[curr_i] = nums[curr_i], nums[i]
                    curr_i += 1
        # last_i = 0
        # for i in range(3):
        #     temp = last_i
        #     for j in range(temp, len(nums)):
        #         if nums[j] == i:
        #             nums[j], nums[last_i] = nums[last_i], nums[j]
        #             last_i += 1

colours = [2, 1, 0]
Solution().sortColors(colours)
print(colours)