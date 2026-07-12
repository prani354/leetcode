class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        left_b = 0
        right_b = 0

        for ch in s:
            if ch == '(':
                left_b += 1

            else:
                right_b += 1

                if left_b > 0:
                    left_b -= 1
                    right_b -= 1

        return left_b + right_b

        