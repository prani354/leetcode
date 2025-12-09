class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        #two hashmap
        memo = {}
        duplets = {}

        res = 0
        MOD = 10 ** 9 + 7

        for num in nums:
            if num in duplets:
                res  = (res + duplets[num]) % MOD   #checking whether it is repeated twice

            twice = num * 2

            if twice in memo:  #counting the numbers
                duplets[twice] = (duplets.get(twice,0) + memo[twice]) % MOD

            memo[num] = memo.get(num,0) + 1

        return res
