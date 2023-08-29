class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd, dvs = abs(dividend), abs(divisor)
        if dvd < dvs:
            return 0
        shift = 0
        while (dvs << (shift + 1)) <= dvd:
            shift += 1
        q = (1 << shift) + self.divide(dvd - (dvs << shift), dvs)
        if (dividend < 0) == (divisor < 0):
            return min((1 << 31) - 1, q)
        return max(-(1 << 31), -q)


print(Solution().divide(10, 3))
