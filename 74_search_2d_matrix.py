from typing import List

# Attempt 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binary_search_row(matrix[self.binary_search_col(matrix, target)], target)
    def binary_search_row(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row)
        while r - l > 1:
            m = (l + r) // 2
            if row[m] > target:
                r = m
            else:
                l = m
        return row[l] == target
    def binary_search_col(self, matrix: List[List[int]], target: int) -> int:
        u, d = 0, len(matrix)
        while d - u > 1:
            m = (u + d) // 2
            if matrix[m][0] > target:
                d = m
            else:
                u = m
        return u

# Attempt 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target: return True
            if target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 23))