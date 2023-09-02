from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        if r == 0:
            return []
        c = len(matrix[0])
        if c == 0:
            return []
        if r == 1:
            return matrix[0]
        if c == 1:
            return [matrix[i][0] for i in range(r)]
        t_row = [matrix[0][i] for i in range(0, c - 1)]
        b_row = reversed([matrix[-1][i] for i in range(1, c)])
        l_col = reversed([matrix[i][0] for i in range(1, r)])
        r_col = [matrix[i][-1] for i in range(0, r - 1)]
        inner = self.spiralOrder([col[1:-1] for col in matrix[1:-1]])
        spiral = []
        spiral.extend(t_row)
        spiral.extend(r_col)
        spiral.extend(b_row)
        spiral.extend(l_col)
        spiral.extend(inner)
        return spiral


print(Solution().spiralOrder([[1, 2], [3, 4]]))
