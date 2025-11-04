class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = 0
        sol = []
        for i in range(n):
            if i + k  <= n:
                c = Counter(nums[i:i+k])
                ans = sorted(c.items(),key = lambda v:(v[1],v[0]),reverse = True)
                #print(ans)
                if len(ans) < x:
                    for r in range(len(ans)):
                        res+=(ans[r][1] * ans[r][0])
                else:
                    for r in range(x):
                        res+=(ans[r][1] * ans[r][0])

                sol.append(res)
                res = 0
        print(sol)
        return sol

        
                
