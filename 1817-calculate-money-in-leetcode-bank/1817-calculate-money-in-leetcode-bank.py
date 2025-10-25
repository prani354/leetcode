class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        ans = 0 
        res = 0
        i = 1

        while i <= n:

            if (i-1) % 7 == 0 and i != 1:
                ans = monday
                monday += 1

            ans += 1
            res += ans
            i += 1

        return res 






        