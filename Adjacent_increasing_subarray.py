class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if 2 * k > n:
            return False
        inc = [1] * n
        for i in range(1, n):
            inc[i] = inc[i - 1] + 1 if nums[i] > nums[i - 1] else 1
        a = 0
        while a + 2 * k <= n:
            r1 = a + k - 1
            r2 = a + 2 * k - 1
            if inc[r1] >= k and inc[r2] >= k:
                return True
            a += 1
        return False
