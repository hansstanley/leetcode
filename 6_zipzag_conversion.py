class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = 2 * numRows - 2
        if d == 0: return s
        output = list()
        for i in range(0, numRows):
            j = i
            k = 0
            is_dup = False
            steps = (d - i * 2, i * 2)
            while j < len(s):
                if not is_dup: output.append(s[j])
                is_dup = steps[k % 2] == 0
                j += steps[k % 2]
                k += 1
        return ''.join(output)

print(Solution().convert('PAYPALISHIRING', 2))