class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        depth = 0 #nested loop

        for i,ch in enumerate(s):

            if ch == '(':
                depth += 1

            else:
                depth -= 1

                if s[i-1] =='(':  #previous index element has open bracket
                    res += (2 ** depth)

        return res