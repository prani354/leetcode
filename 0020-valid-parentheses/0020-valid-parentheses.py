class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { '}':'{' , ')':'(', ']':'['}

        for ch in s:

            if ch in hashmap:
                if not stack and stack[-1] != hashmap[ch]:
                    return False

                
                stack.pop()

            else:  
                stack.append(ch)

        return len(stack) == 0

                