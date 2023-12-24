import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return self.helper(list(range(1, n + 1)), k, math.factorial(n - 1))

    def helper(self, nums: list[int], k: int, fact: int) -> str:
        i = math.ceil(k / fact) - 1
        curr = str(nums[i])
        nums.pop(i)
        return curr + (
            ""
            if len(nums) == 0
            else self.helper(
                nums,
                k % fact,
                fact // len(nums),
            )
        )


print(Solution().getPermutation(3, 6))
