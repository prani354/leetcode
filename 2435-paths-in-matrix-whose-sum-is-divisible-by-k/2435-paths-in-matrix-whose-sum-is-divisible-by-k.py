class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[j][r] = ways to reach current row, column j, with remainder r
        dp = [[0] * k for _ in range(n)]

        dp[0][grid[0][0] % k] = 1

        for i in range(m):
            new_dp = [[0] * k for _ in range(n)]
            for j in range(n):
                for r in range(k):
                    if j > 0:  # from left
                        nr = (r + grid[i][j]) % k
                        new_dp[j][nr] = (new_dp[j][nr] + new_dp[j-1][r]) % MOD
                    if i > 0:  # from top
                        nr = (r + grid[i][j]) % k
                        new_dp[j][nr] = (new_dp[j][nr] + dp[j][r]) % MOD
                # handle first cell separately
                if i == 0 and j == 0:
                    new_dp[0] = dp[0]
            dp = new_dp
        
        return dp[n-1][0]