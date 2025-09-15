class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
    
        for i in range(n):
        
            while stack and stack[-1][0] < temperatures[i]:
                t , idx = stack.pop()
                ans[idx] = i - idx

            stack.append((temperatures[i],i))

        return ans

        