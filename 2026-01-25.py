class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 1. Sorting allows us to compare k-sized groups efficiently
        nums.sort()
        
        # 2. Handle the base case where k is 1
        if k == 1: return 0
        
        res = float('inf')
        
        # 3. Slide a window of size k across the sorted list
        # The range should stop at len(nums) - k + 1
        for i in range(len(nums) - k + 1):
            # Difference between the highest (i + k - 1) and lowest (i) in the window
            diff = nums[i + k - 1] - nums[i]
            res = min(res, diff)
            
        return res
