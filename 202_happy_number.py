class Solution:
    def isHappy(self, n: int) -> bool:
        met = set[int]()
        while n != 1:
            if n in met:
                break
            met.add(n)
            n = sum(map(lambda x: int(x) ** 2, str(n)))
        return n == 1
