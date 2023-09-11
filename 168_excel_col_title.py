class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            c = columnNumber % 26 or 26
            title = chr(c + 64) + title
            print(columnNumber, c, title)
            columnNumber //= 26
        return title


print(Solution().convertToTitle(28))
