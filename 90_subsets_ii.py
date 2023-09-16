from typing import List, Set, Tuple


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return [list(c) for c in self.collect(sorted(nums))]

    def collect(self, nums: List[int], i: int = 0) -> Set[Tuple[int, ...]]:
        if i == len(nums):
            return set()
        if i == len(nums) - 1:
            return {(), (nums[i],)}
        choices_without = self.collect(nums, i + 1)
        choices_with = {(nums[i], *c) for c in choices_without}
        return {*choices_without, *choices_with}


print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
