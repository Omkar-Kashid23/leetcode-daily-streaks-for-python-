class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i == "(":stack.append(0)
            elif stack:
                last_score = stack.pop()
                stack[-1] += max(1,last_score * 2)
        return stack[-1]
