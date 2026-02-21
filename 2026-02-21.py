class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num  % i ==0:
                    return False
            return True
        cnt = 0
        for i in range(left,right+1):
            res = str(bin(i)[2:])
            if is_prime(res.count('1')):
                cnt += 1
        return cnt
