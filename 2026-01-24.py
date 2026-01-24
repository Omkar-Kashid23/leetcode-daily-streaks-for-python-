class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        lst = []
        left = 0
        right = len(nums) - 1
        while(left<right):
            i = nums[left]
            left += 1
            j = nums[right]
            right -= 1
            lst.append(i+j)
        return max(lst)
