class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        for i,j in pairwise(nums):
            if j == i+1:total +=j
            else:break
        num_set = set(nums)
        while total in num_set:total += 1
        return total