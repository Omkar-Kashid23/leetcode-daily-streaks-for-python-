class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        depth = 0
        for i in s:
            if i == "(":
                depth += 1
                if depth > 1:
                    res += i
            elif i == ")":
                depth -= 1
                if depth > 0:
                    res += i
        return res
