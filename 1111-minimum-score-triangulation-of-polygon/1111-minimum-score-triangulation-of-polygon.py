class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(2,n):
            for j in range(n-i):
                l = j + i
                b = float('inf')
                for k in range(1+j,l):
                    s = dp[j][k] + dp[k][l] + values[j] * values[k] * values[l]
                    b = min(b,s)
                dp[j][l] = b
        return dp[0][n-1]