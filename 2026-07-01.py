class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cnt = 0
        n = len(cost)
        cost.sort(reverse = True)
        for i in range(n):
            if (i+1) % 3 == 0:
                continue
            else:
                cnt += cost[i]
        return cnt
