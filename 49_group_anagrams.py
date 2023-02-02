from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = [str(sorted(s)) for s in strs]
        anagrams = {}
        for k, s in zip(keys, strs):
            anagrams.setdefault(k, [])
            anagrams[k].append(s)
        return anagrams.values()