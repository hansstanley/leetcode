from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])

        def traverse(r: int, c: int, up: bool = True):
            path = list[int]()
            if up:
                while r >= 0 and c < cols:
                    path.append(mat[r][c])
                    r -= 1
                    c += 1
                r += 1
                c -= 1
                if c < cols - 1:
                    c += 1
                else:
                    r += 1
            else:
                while r < rows and c >= 0:
                    path.append(mat[r][c])
                    r += 1
                    c -= 1
                r -= 1
                c += 1
                if r < rows - 1:
                    r += 1
                else:
                    c += 1
            return path, r, c

        order = list[int]()
        up = True
        row, col = 0, 0
        while (row, col) != (rows - 1, cols - 1):
            path, row, col = traverse(row, col, up)
            order.extend(path)
            up = not up
        order.append(mat[row][col])
        return order
