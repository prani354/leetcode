class Solution:
    def maxOperations(self, s: str) -> int:
        one_count = 0 
        res = 0

        for i in range(len(s)):

            if s[i] == '1':
                one_count += 1

            else:
                if i > 0 and s[i-1] == '1':
                    res += one_count

        return res
        