class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for price in prices:
            if price > buy:
                p = price - buy
                profit = max(profit,p)

            else:
                buy = price
        return profit
