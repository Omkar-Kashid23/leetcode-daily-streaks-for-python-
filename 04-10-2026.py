class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if len(open_stack) > 0:
                    open_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                else:
                    return False
        while len(open_stack) > 0 and len(star_stack) > 0:
            open_idx = open_stack.pop()
            star_idx = star_stack.pop()
            if open_idx > star_idx:
                return False
        return len(open_stack) == 0
