class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.parse(s) == self.parse(t)
    def parse(self, s: str) -> str:
        arr = []
        for c in s:
            if c == '#':
                if len(arr) > 0: arr.pop()
            else:
                arr.append(c)
        return ''.join(arr)
