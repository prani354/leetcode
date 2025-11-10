class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [-1]
        operation = 0

        for num in nums:
            while num < stack[-1]:
                stack.pop()
            
            if num > stack[-1]:
                operation += (num > 0)
                stack.append(num)

        return operation

            
        