class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]

        stack = []
        # golden rule: three elements at most in the stack
        # at all times
        for t in tokens:
            if t in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                result = 0
                match t:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = int(num1 / num2)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack[0]