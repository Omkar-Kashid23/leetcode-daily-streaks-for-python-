class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        ite = 0
        for i in costs:
            cnt += i
            if cnt <= coins:
                ite += 1
        return ite