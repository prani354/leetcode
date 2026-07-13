class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for files in logs:
            if files == './':
                continue

            if stack and files == '../':
                stack.pop()

            if files != './' and files != '../':
                stack.append(files)

        print(stack)
        return len(stack)