class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # dp[i][j][s] = number of ways to reach (i,j) with sum % k == s
        dp = [[[0] * k for _ in range(c)] for _ in range(r)]
        
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(r):
            for j in range(c):
                for s in range(k):
                    if dp[i][j][s] > 0:
                        if i + 1 < r:
                            ns = (s + grid[i+1][j]) % k
                            dp[i+1][j][ns] = (dp[i+1][j][ns] + dp[i][j][s]) % MOD
                        if j + 1 < c:
                            ns = (s + grid[i][j+1]) % k
                            dp[i][j+1][ns] = (dp[i][j+1][ns] + dp[i][j][s]) % MOD
        
        return dp[r-1][c-1][0]
