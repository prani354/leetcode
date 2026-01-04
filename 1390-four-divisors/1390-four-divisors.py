import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            #i = 1
            #divisor = 0
            ans = []
            for i in range(1,math.isqrt(num) + 1):
                if  num % i == 0:
                    ans.append(i)
                    val = num // i
                    if val != i:
                        ans.append(val)

            if len(ans) == 4:
                res += sum(ans)

        return res


