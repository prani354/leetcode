class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        if n % 2 == 0: return True

        dp = list(piles)

        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                dp[j] = max(nums[i]-dp[j],nums[j]-dp[j+1])

        return dp[-1] >= 0
