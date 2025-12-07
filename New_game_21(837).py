class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        # Initialize dp array to store probabilities.
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        # window_sum tracks the sum of probabilities for the last maxPts scores.
        window_sum = 1.0
        
        # ans will store the total probability of winning.
        ans = 0.0
        
        # Iterate from score 1 up to n.
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            
            if i < k:
                # If current score is less than k, Alice continues to draw.
                window_sum += dp[i]
            else:
                # If current score is k or more, she stops.
                ans += dp[i]
            
            # Remove the probability of the score that is now out of the window.
            # This is the optimization for the sliding window.
            if i >= maxPts:
                window_sum -= dp[i - maxPts]
                
        return ans
