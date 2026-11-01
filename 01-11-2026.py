class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_ele = min(nums)
        return sum(num - min_ele for num in nums)
