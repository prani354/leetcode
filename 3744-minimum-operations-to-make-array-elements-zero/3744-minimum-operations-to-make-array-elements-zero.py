class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0

        def till(n):
            if n <= 0:
                return 0
            total = 0
            k = 0
            start = 1

            while start <= n:
                end = min(n,4**(k+1)-1)
                count = end - start + 1
                total += count*(k+1)
                start *= 4
                k += 1
            return total

        for x,y in queries:
            steps = till(y) - till(x-1)
            res += (steps+1)//2

        return int(res)

        
        