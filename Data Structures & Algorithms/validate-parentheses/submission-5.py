class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = [] 
        for c in s:
            if c in brackets.keys():
                if len(stack) == 0 or stack.pop() != brackets[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0