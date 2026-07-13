class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:

            while stack and stack[-1] == ch:
                stack.pop()
                break

            else:
                stack.append(ch)

        return "".join(stack)