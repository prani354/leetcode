class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 1
        dp = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):

                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = 1 + dp[j]
                    count[i] = count[j]

                elif nums[i] > nums[j] and dp[i] == 1 + dp[j]:
                    count[i] += count[j]

            max_value = max(max_value,dp[i])

        res = 0

        for i in range(n):
            if max_value == dp[i]:
                res += count[i]

        return res

            
                    


    