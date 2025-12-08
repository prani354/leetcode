import math
class Solution:
    def countTriples(self, n: int) -> int:
        output = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if i*i + j*j == k*k:
                        output += 2
        return output

            

        