from functools import cmp_to_key
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def compare(a: int, b: int):
            if a == b:
                return 0
            if a == 0:
                return -1
            if b == 0:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare), reverse=True)
