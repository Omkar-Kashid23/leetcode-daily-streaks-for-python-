class Solution:
    def numSteps(self, s: str) -> int:
        num = int(str(s),2)
        cnt = 0
        while(num > 1):
            if num % 2 != 0:
                cnt += 1
                num += 1
            else:
                num //= 2
                cnt +=1
        return cnt
