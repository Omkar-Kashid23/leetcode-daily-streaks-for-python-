class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if q:=nums.count(1): return n-q
        return next((w+n-2 for w in range(n+1) for i in range (n-w+1)if gcd(*nums[i:i+w])==1),-1)
