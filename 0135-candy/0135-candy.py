class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1] * n

        #left to right traversal
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1]+1

        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                res[j] = max(res[j],res[j+1]+1)

        return sum(res)        
        