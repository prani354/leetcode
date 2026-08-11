class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = { '}':'{' , ')':'(', ']':'['}

        if not s: return True

        for ch in s:
            if ch in hashmap:
                if not stack or hashmap[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(ch)

        return stack == []

        