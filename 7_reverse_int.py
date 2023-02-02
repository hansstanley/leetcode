class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        x, result = abs(x), 0
        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
        result = neg * result
        if -(2**31) <= result <= (2**31) - 1:
            return result
        else:
            return 0


print(-(2 ** 31), (2**31) - 1)
print(Solution().reverse(321))
print(Solution().reverse(-321))
print(Solution().reverse(1534236469))
print(Solution().reverse(1563847412))
