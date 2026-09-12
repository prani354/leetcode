#from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_amount = amount + 1

        dp = [max_amount] * (max_amount)
        dp[0] = 0

        for i in range(1,len(dp)):
            for coin in coins:

                if coin <= i:
                    dp[i] = min(dp[i] , 1 + dp[i-coin])

        if dp[amount] == max_amount: return -1

        return dp[amount]

