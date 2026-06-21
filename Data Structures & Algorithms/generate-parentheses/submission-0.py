class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(s: str, openP: int, closeP: int):
            if openP == closeP == n:
                result.append(s)
                return
            elif openP <= n and closeP <= n:
                if closeP < openP:
                    helper(s + ")", openP, closeP+1)
                helper(s + "(", openP+1, closeP)
        helper("(", 1, 0)
        return result;

    