class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) == len(nums):
            return len(nums) - 1
        if sum(nums) == 0:
            return 0

        l, r = 0, 0
        zeros_count = 0
        zero_idx = -1
        max_len = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                if zeros_count == 0:
                    zeros_count += 1
                    zero_idx = r
                else:
                    max_len = max(max_len, r - l - 1)
                    l = zero_idx + 1
                    zero_idx = r
                    zeros_count = 1
        if nums[r] == 1: max_len = max(max_len, r - l)
        return max_len
        
