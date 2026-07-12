class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"

        stack = []

        for ch in num:

            while stack and ch < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            
            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        res = "".join(stack).lstrip('0')

        if res != "":
            return res

        return "0"