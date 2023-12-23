from typing import Dict, List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict: Dict[int, bool] = dict([(x, True) for x in nums])
        for x in nums_dict.keys():
            if x - 1 in nums_dict:
                nums_dict[x] = False
        count_max = 0
        for x in nums_dict.keys():
            if not nums_dict[x]:
                continue
            i = 1
            while x + i in nums_dict:
                i += 1
            count_max = max(count_max, i)
        return count_max
