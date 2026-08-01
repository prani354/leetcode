class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True

        dp = list(nums)
        #print(dp)
        for i in range(n-2,-1,-1):
            print(i)
            for j in range(i+1,n):
                print(j)
                dp[j] = max(nums[i] - dp[j],nums[j] - dp[j-1])
                print(dp[j])

        return dp[-1] >= 0