from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, init_color: int = None) -> List[List[int]]:
        m, n = len(image), len(image[0])
        if sr < 0 or sr >= m: return image
        if sc < 0 or sc >= n: return image
        if image[sr][sc] == color: return image

        if init_color is None: init_color = image[sr][sc]
        if init_color == image[sr][sc]:
            image[sr][sc] = color
        else:
            return image
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.floodFill(image, sr + dr, sc + dc, color, init_color)
        return image