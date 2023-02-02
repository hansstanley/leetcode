class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        res = []
        for c in prev:
            if len(res) == 0 or res[-1][0] != c:
                res.append([c, 1])
            else:
                res[-1][1] += 1
        s = ""
        for c, i in res:
            s += str(i) + c
        return s


for i in range(5):
    print(Solution().countAndSay(i + 1))
