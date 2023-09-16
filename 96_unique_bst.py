class Solution:
    def numTrees(self, n: int) -> int:
        bsts = [1, 1]
        for i in range(2, n + 1):
            left, right = 0, i - 1
            count = 0
            while left < right:
                count += bsts[left] * bsts[right] * 2
                left += 1
                right -= 1
            if left == right:
                count += bsts[left] * bsts[right]
            bsts.append(count)
        return bsts[n]
