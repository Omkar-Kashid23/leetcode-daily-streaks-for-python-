class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k
    # Alternative Answer
        max_value = nums[0]
        min_value = nums[0]
        for i in nums:
            if i > max_value:max_value = i
            if i < min_value:min_value = i
        return (max_value - min_value) * k