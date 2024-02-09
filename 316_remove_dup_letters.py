class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = dict[str, int]()
        seen = dict[str, bool]()
        res = list[str]()
        for i, c in enumerate(s):
            last[c] = i
            seen[c] = False
        for i, c in enumerate(s):
            if seen[c]:
                continue
            while len(res) > 0:
                if res[-1] <= c:
                    break
                if last[res[-1]] < i:
                    break
                seen[res[-1]] = False
                res.pop()
            seen[c] = True
            res.append(c)
        return "".join(res)


print(Solution().removeDuplicateLetters("bcabc"))
