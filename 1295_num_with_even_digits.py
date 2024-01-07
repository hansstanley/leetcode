from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            count += 1 if self.has_even_number_of_digits(num) else 0
        return count

    def has_even_number_of_digits(self, num: int) -> bool:
        return len(str(num)) % 2 == 0
