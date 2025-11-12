import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if 1 in nums:
            return n - nums.count(1)

        maxx = 0

        for num in nums:
            maxx = math.gcd(maxx,num)

        if maxx > 1:
            return -1

        count = n

        for i in range(n):
            g = nums[i]

            for j in range(i+1,n):
                g = math.gcd(g,nums[j])

                if g == 1:
                    count = min(count,j-i)
                    break

        return count + (n-1)

        