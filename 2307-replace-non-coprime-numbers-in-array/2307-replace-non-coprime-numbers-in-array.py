import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stk = []

        for num in nums:

            while stk and math.gcd(stk[-1],num) > 1:
                top = stk.pop() 
                num = (top*num) // math.gcd(top,num)

            stk.append(num)

        return stk
        