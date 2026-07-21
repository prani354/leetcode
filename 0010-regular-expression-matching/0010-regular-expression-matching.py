class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # cache = {}

        # def dfs(i,j):
            
        #     if (i,j) in cache:
        #         return cache[(i,j)]
        #     if i >= len(s) and j >= len(p):
        #         return True

        #     if j >= len(p):
        #         return False

        #     match = (i < len(s) and (s[i] == p[j] or p[j] == '.'))

        #     if (j+1) < len(p) and p[j+1] == '*':
        #         cache[(i,j)] = (dfs(i,j+2) # * not used
        #         or (match and dfs(i+1,j))) # * used

        #         return cache[(i,j)]

        #     if match: 
        #         cache[(i,j)] = dfs(i+1,j+1)
        #         return cache[(i,j)] 

        #     cache[(i,j)] = False

        #     return False

        # return dfs(0,0)
        m , n = len(s) , len(p)

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True  # Both s and p are empty

        for j in range(1,n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]

        return dp[m][n]