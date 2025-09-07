class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        if n % 2 != 0:
            res.append(0)

        x = n // 2

        for i in range(1,x+1):
            res.append(i)
            res.append(-i)

        return res


        
        