class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10**9 + 7
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # 1. Base Cases: Arrays made entirely of 1s or entirely of 0s
        # We can only build these up to our 'limit'
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
            
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # 2. Build the arrays from left to right
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                
                # --- Calculate arrays ending in 0 ---
                # Add a 0 to all previous valid arrays (both ending in 0 and 1)
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod
                
                # If we have placed more 0s than the limit, subtract the invalid sequences
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]) % mod
                
                # --- Calculate arrays ending in 1 ---
                # Add a 1 to all previous valid arrays
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % mod
                
                # If we have placed more 1s than the limit, subtract the invalid sequences
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0]) % mod
                    
        # 3. The answer is the sum of valid arrays ending in 0 and ending in 1
        return (dp[zero][one][0] + dp[zero][one][1]) % mod
        
