class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] > target:break
            if nums[i] == target:res.append(i)
        return res
