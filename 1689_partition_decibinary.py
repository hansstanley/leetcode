class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(c) for c in n])


# Previous attempt
class Solution1:
    def minPartitions(self, n: str) -> int:
        digits = [int(c) for c in n]
        count = 0
        while len(digits) > 0:
            left = len(digits)
            count += 1
            for i in range(len(digits)):
                if digits[i] > 0:
                    digits[i] -= 1
                if digits[i] > 0 and i < left:
                    left = i
            digits = digits[left:]
        return count
