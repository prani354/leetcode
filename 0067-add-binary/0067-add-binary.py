class Solution:
    def addBinary(self, a: str, b: str) -> str:
        val1 = int(a,2)
        val2 = int(b,2)
        add = val1 + val2

        return bin(add)[2:]
         