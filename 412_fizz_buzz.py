from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [""] * n
        for i in range(1, n + 1):
            if i % 3 == 0:
                arr[i - 1] += "Fizz"
            if i % 5 == 0:
                arr[i - 1] += "Buzz"
            if not arr[i - 1]:
                arr[i - 1] = str(i)
        return arr
