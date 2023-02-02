class Solution:
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        a1, a2 = list(num1), list(num2)
        a1.reverse()
        a2.reverse()
        product = 0
        for i, c1 in enumerate(a1):
            for j, c2 in enumerate(a2):
                product += self.digits[c1] * self.digits[c2] * (10**(i + j))
        return str(product)

print(Solution().multiply('123', '456'))