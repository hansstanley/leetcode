from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [[x] for x in nums]
        perms = []
        for i, x in enumerate(nums):
            ps = self.permute([*nums[:i], *nums[i + 1 :]])
            for p in ps:
                p.append(x)
            perms.extend(ps)
        return perms
