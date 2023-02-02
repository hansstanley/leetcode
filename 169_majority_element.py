from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m, i = 0, 0
        for x in nums:
            m, i = (
                x if i == 0 else m,
                i + 1 if i == 0 or m == x else i - 1
            )
        return m

print(Solution().majorityElement([2,2,1,1,1,2,2]))
print(Solution().majorityElement([3,2,3]))