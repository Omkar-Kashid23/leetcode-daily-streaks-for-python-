class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            divisors = []

            for x in range(1, int(num**0.5) + 1):
                if num % x == 0:
                    divisors.append(x)
                    if x != num // x:
                        divisors.append(num // x)

                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                res += sum(divisors)

        return res
