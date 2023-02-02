from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        count, curr_furthest, next_furthest = 0, 0, 0
        for i, n in enumerate(nums[:-1]):
            next_furthest = max(next_furthest, i + n)
            if i == curr_furthest:
                curr_furthest = next_furthest
                count += 1
        return count

# Attempt 1 (too slow)
class Solution1:
    def jump(self, nums: List[int]) -> int:
        memo = {len(nums) - 1: 0}
        for i in range(len(nums) - 2, -1, -1):
            memo[i] = -1
            if nums[i] == 0: continue
            for j in range(1, 1 + nums[i]):
                if i + j >= len(nums): break
                if memo[i + j] < 0: continue
                memo[i] = 1 + memo[i + j] if memo[i] < 0 else min(
                    memo[i],
                    memo[i + j] + 1
                )
        return memo[0]

print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,0,1,4]))
print(Solution().jump([2,1,0]))
print(Solution().jump([2,1]))
print(Solution().jump([2]))