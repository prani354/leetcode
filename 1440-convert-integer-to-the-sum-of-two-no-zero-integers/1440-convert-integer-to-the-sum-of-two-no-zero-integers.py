class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def noZero(x):
            while x > 0:
                if x % 10 == 0:
                    return False
                x //= 10
            return True

        for a in range(1,n):
            b = n - a
            if noZero(a) and noZero(b):
                return [a,b]

        return []
        
        