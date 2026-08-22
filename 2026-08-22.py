class Solution:
    def checkDivisibility(self, n: int) -> bool:
        lst = [int(i) for i in str(int(n))]
        cnt = 1
        for i in lst:
            cnt *= i
        return n % ((sum(lst)) + cnt) == 0
