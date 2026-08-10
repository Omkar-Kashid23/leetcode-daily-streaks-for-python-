class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1) 
        sq = []
        cursq = 1
        for i in range(1,n+1):
            if i == cursq * cursq:
                sq.append(i)
                cursq += 1
                dp[i] = True
            else:
                for sqr in sq:
                    if not dp[i - sqr]:
                        dp[i] = True
                        break
        return dp[n]