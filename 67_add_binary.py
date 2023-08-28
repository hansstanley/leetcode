class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or a == "0":
            return b
        if not b or b == "0":
            return a
        carry = "0"
        res = ""
        j = -1
        for i in range(-1, -min(len(a), len(b)) - 1, -1):
            j = i
            if a[i] == b[i]:
                res = carry + res
                carry = "0" if a[i] == "0" else "1"
            else:
                if carry == "0":
                    res = "1" + res
                else:
                    res = "0" + res
                    carry = "1"
        res_left = self.addBinary(carry, a[:j] or b[:j])
        return res_left + res
