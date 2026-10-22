class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:return 0
        st = nums.index(0)
        asc = True
        desc = True
        for i in range(1,n):
            value = nums[(st + i)%n]
            if value != i:asc = False
            if value != n - i:desc = False
            if not asc and not desc:return -1
        if asc:return min(st,n-st+2)
        return min(n-st,st + 2)
