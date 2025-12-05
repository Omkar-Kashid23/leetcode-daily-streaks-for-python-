class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt = 0
        prefix_sum = 0 
        total = sum(nums)
        for i in range(len(nums)-1):
            prefix_sum += nums[i]
            suffix_sum = total - prefix_sum
            if (suffix_sum-prefix_sum)%2 == 0:
                cnt += 1
        return cnt
