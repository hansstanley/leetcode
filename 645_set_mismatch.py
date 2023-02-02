from typing import List

<unsolved>
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.reverse()
        missing: int = None
        dup: int = None
        prev: int = None
        for i in range(1, len(nums) + 1):
            curr = nums[-1]
            