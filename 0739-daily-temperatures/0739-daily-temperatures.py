class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        for i in range(len(temperatures)-1,-1,-1):

            while stack:
                if temperatures[i] < stack[-1][0]:
                    res.append(stack[-1][1] - i)
                    stack.append((temperatures[i],i))
                    break
                else:
                    stack.pop()

            if not stack:
                res.append(0)
                stack.append((temperatures[i],i))

        return res[::-1]

