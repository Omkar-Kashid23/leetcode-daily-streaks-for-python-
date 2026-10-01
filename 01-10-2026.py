class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        if len(s) == 1:
            return False
        if s[0] in '])}':return False
        for i in s:
            if i in '([{':
                lst.append(i)
            else:
                if len(lst) == 0:return False
                elif i == ']' and lst[-1] == '[':
                    lst.pop()
                elif i == ')' and lst[-1] == '(':
                    lst.pop()
                elif i == '}' and lst[-1] == '{':
                    lst.pop()
                else: return False
        if len(lst)==0: return True        
        return False
