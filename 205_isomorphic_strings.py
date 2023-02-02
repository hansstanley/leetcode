class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c_map = {}
        s, t = list(s), list(t)
        for i, (j, k) in enumerate(zip(s, t)):
            if not c_map.get(j):
                if k in c_map.values(): return False
                c_map[j] = k
            s[i] = c_map[j]
        return s == t