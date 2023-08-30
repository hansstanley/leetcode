from typing import List, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(self.helper(nums))

    def helper(self, nums: List[int]) -> Tuple[int, int, int, int]:
        if len(nums) == 0:
            return 0, 0, 0, 0
        if len(nums) == 1:
            return nums[0], nums[0], nums[0], nums[0]
        mid = len(nums) // 2
        ll, lm, lr, l_local = self.helper(nums[:mid])
        rl, rm, rr, r_local = self.helper(nums[mid:])
        local_l = max(lm, lr)
        local_r = max(rl, rm)
        if local_l < 0 or local_r < 0:
            local = max(local_l, local_r)
        else:
            local = local_l + local_r
        return (
            max(ll, lm + max(rl, rm, 0)),
            lm + rm,
            max(rr, rm + max(lr, lm, 0)),
            max(l_local, r_local, local),
        )

    # def maxSubArray(self, nums: List[int], curr: int = 0) -> int:
    #     if len(nums) == 0:
    #         return curr
    #     return max(
    #         self.maxSubArray(nums[1:], curr + nums[0]),
    #         self.maxSubArray(nums[1:], nums[0]),
    #     )


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
