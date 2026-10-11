class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        cnt = nums[0]**2
        n = len(nums)
        for i in range(2,n+1):
            if n % i == 0:
                cnt += nums[i-1]**2
        return cnt
