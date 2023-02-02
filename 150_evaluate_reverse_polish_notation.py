from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    stack.append(int(t))
        return stack.pop()

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))