from typing import List


class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lo, hi = 0, len(m) - 1
        while hi - lo > 0:
            for i in range(0, hi - lo):
                m[lo][lo + i], m[lo + i][hi], m[hi][hi - i], m[hi - i][lo] = (
                    m[hi - i][lo],
                    m[lo][lo + i],
                    m[lo + i][hi],
                    m[hi][hi - i],
                )
            lo += 1
            hi -= 1


# Solution().rotate(
#     [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16],
#     ]
# )
Solution().rotate(
    [
        [2, 29, 20, 26, 16, 28],
        [12, 27, 9, 25, 13, 21],
        [32, 33, 32, 2, 28, 14],
        [13, 14, 32, 27, 22, 26],
        [33, 1, 20, 7, 21, 7],
        [4, 24, 1, 6, 32, 34],
    ]
)
# Solution().rotate(
#     [
#         [27, 9, 25, 13],
#         [33, 32, 2, 28],
#         [14, 32, 27, 22],
#         [1, 20, 7, 21],
#     ]
# )
