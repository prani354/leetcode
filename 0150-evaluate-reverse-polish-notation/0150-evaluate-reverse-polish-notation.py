class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for exp in tokens:
            if exp == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                res = val1 + val2
                stack.append(res)
            elif exp == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                res =  val2 - val1
                stack.append(res)
            elif exp == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                res = val1 * val2
                stack.append(res)
            elif exp == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                res = int(val2 / val1)
                stack.append(res)
            else:
                stack.append(int(exp))
        return stack[0]
