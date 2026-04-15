class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        valid_ops = ['+', '-', '*', '/']

        stack = []

        res = 0
        for i in range(len(tokens)):
            if tokens[i] not in valid_ops:
                stack.append(tokens[i])
            else:
                if tokens[i] == '+':
                    res = int(stack.pop()) + int(stack.pop())
                elif tokens[i] == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    res = b - a
                elif tokens[i] == '*':
                    res = int(stack.pop()) * int(stack.pop())
                elif tokens[i] == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    res = int(b/a)
                
                stack.append(int(res))
        
        return int(stack[0])