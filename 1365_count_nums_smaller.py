from typing import List

import numpy as np


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr_nums = np.array(nums, dtype=np.int32)
        counts = np.zeros(arr_nums.shape, dtype=np.int32)
        for x in nums:
            counts += (arr_nums - x).clip(min=0, max=1)
        return counts.tolist()


print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
