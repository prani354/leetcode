class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Define LCS

        n = len(str1)
        m = len(str2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):

                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        # Construct SCS

        i = n
        j = m
        res = []
        while i > 0 and j > 0:

            if str1[i-1] == str2[j-1]:
                res.append(str1[i-1]) #Taking common character
                i -= 1
                j -= 1

            
            elif dp[i-1][j] > dp[i][j-1]:
                res.append(str1[i-1])
                i -= 1

            else:
                res.append(str2[j-1])
                j -= 1

        #Adding remaining characters
        while i > 0:
            res.append(str1[i-1])
            i -= 1

        while j > 0:
            res.append(str2[j-1])
            j -= 1

        return "".join(res[::-1])



                
                    


