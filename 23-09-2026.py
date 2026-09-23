class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target,n = sum(nums) - x,len(nums)
        if target == 0:return n
        max_len = curr_sum = left = 0
        for right, val in enumerate(nums):
            curr_sum += val
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len,right - left + 1)
        return n - max_len if max_len else -1
