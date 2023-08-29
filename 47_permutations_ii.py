from typing import List, Set, Tuple


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = self.permute(nums)
        return [list(p) for p in perms]

    def permute(self, nums: List[int]) -> Set[Tuple[int]]:
        if len(nums) <= 1:
            return {(x,) for x in nums}
        perms: Set[Tuple[int]] = set()
        for i, x in enumerate(nums):
            ps = self.permute([*nums[:i], *nums[i + 1 :]])
            ps = {(x, *p) for p in ps}
            perms = perms.union(ps)
        return perms
