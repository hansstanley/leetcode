class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = dict[str, int]()
        c_map = dict[str, int]()
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
            c_map[c] = 0
        count = len(t)
        beg, end = 0, 0
        head, length = 0, len(s) + 1
        while end < len(s):
            if s[end] in t_map:
                c_map[s[end]] += 1
                if c_map[s[end]] <= t_map[s[end]]:
                    count -= 1
            end += 1
            while count == 0:
                if (end - beg) < length:
                    head, length = beg, end - beg
                if s[beg] in t_map:
                    c_map[s[beg]] -= 1
                    if c_map[s[beg]] < t_map[s[beg]]:
                        count += 1
                beg += 1
        return "" if length == (len(s) + 1) else s[head : head + length]


print(Solution().minWindow("a", "a"))
