class Solution:
    def numDecodings(self, s: str) -> int:
        count0, count1, count2 = 0, 0 if s[-1] == "0" else 1, 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "0":
                count0 = 0
            else:
                count0 += count1
                if int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i + 1]) < 7):
                    count0 += count2
            count0, count1, count2 = 0, count0, count1
        return count1


print(Solution().numDecodings("1201234"))
