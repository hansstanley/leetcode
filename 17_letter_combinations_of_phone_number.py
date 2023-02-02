from typing import List


class Solution:
    letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    combs: List[str] = []
    def letterCombinations(self, digits: str) -> List[str]:
        self.combs.clear()
        if len(digits) != 0: self.helper(digits, '')
        return self.combs
    def helper(self, digits: str, comb: str):
        if len(digits) == 0:
            self.combs.append(comb)
            return
        next_digits = digits[1:]
        for c in self.letters[digits[0]]:
            self.helper(next_digits, comb + c)