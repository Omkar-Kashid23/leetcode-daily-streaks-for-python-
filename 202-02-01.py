class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first_val = nums[0]
        val_1, val_2 = min(nums[1], nums[2]), max(nums[1], nums[2])
        for i in range(3, len(nums)):
            if val_1 > nums[i]:
                val_1, val_2 = nums[i], val_1
            elif val_2 > nums[i]:
                val_2 = nums[i]
        return first_val + val_1 + val_2
