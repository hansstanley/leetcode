from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return
    def helper(self, s: str, l: int):
        bal = 0
        r = len(s)
        for i, c in enumerate(s[l:]):
            if c == '(':
                bal += 1
            elif c == ')':
                bal -= 1
            if bal < 0:
                r = i + l + 1
                break
        
