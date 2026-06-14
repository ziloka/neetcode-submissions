class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if you see n1, n2, operator
        # it is time to unravel

        # invariants
        # end of loop consists of the last thing computed

        operators = ["+", "-", "*", "/"]
        stack = []
        for t in tokens:
            if len(stack) != 0 and t in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                result = 0
                match t:
                    case "+":
                        result = n2 + n1 
                    case "-":
                        result = n2 - n1
                    case "*":
                        result = n2 * n1
                    case "/":
                        result = int(n2 / n1)
                stack.append(result)
            else:
                stack.append(int(t))

        return stack[0]

        # 1, 2, + , 3, *, 4, -
        # 3
        # 3, 3, *
        # 9
        # 9, 4 -
        # 5