class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        num = list(num)

        if len(num) == k:
            return "0"
        for n in num:

            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1

        res = "".join(stack).lstrip('0')

        if res != "":
            return res

        return "0"
