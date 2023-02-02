class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        subs = []
        curr = set()
        left = 0
        for i, c in enumerate(s):
            if c in curr:
                subs.append(s[left:i])
                while s[left] != c:
                    curr.remove(s[left])
                    left += 1
                curr.remove(c)
                left += 1
            curr.add(c)
        subs.append(s[left:])
        return max([len(sub) for sub in subs])


print(Solution().lengthOfLongestSubstring(' '))
