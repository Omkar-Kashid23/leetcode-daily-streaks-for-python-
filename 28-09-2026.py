class Solution:
    def maxDepth(self, s: str) -> int:
        lst = []
        cnt = 0
        for i in s:
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            lst.append(cnt)
        return max(lst)
        # return max(lst[i for i in s:])
