class Solution:
    def minScoreTriangulation(self, A: list[int]) -> int:
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        for length in range(2,n):
            for i in range(n-length):
                j = i+length
                dp[i][j] = min(dp[i][k]+dp[k][j]+A[i]*A[k]*A[j] for k in range(i+1,j))
        return dp[0][n-1]
