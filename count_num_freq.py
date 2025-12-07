class Solution:
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        maxf = max(freq.values())
        return sum(v for v in freq.values() if v == maxf)

nums1 = [1,2,2,3,1,4]
nums2 = [1,2,3,4,5]

print(Solution().maxFrequencyElements(nums1))
print(Solution().maxFrequencyElements(nums2))
