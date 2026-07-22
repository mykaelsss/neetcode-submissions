import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if self.is_number(t):
                stack.append(int(t))
            else:
                num2, num1 = stack.pop(), stack.pop()
                eval = self.handleEquation(num1, num2, t)
                stack.append(eval)
        return stack[-1]
    
    def handleEquation(self, num1: int, num2: int, operator: str) -> int:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return math.trunc(num1 / num2)
            case _:
                return 0

    def is_number(self, s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False