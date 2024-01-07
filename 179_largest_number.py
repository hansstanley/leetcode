from functools import cmp_to_key
from typing import List


def compare(a: int, b: int):
    return int(str(a) + str(b)) - int(str(b) + str(a))


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = "".join(
            map(
                str,
                sorted(
                    nums,
                    key=cmp_to_key(compare),
                    reverse=True,
                ),
            )
        ).lstrip("0")
        return res if res else "0"
