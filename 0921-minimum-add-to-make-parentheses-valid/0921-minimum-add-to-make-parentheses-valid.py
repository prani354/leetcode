class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        lb = 0
        rb = 0

        for ch in s:
            if ch == '(':
                lb += 1

            else:
                if lb > 0:
                    lb -= 1

                else:
                    rb += 1

        return rb + lb