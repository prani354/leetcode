class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        depth = 0 #nested loop

        for i,ch in enumerate(s):

            if ch == '(':
                depth += 1

            else:
                depth -= 1

                if s[i-1] == '(': #Stack check to find it is nested
                    res += (2 ** depth)

        return res        