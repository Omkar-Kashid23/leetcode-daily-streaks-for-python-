from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        most_common_value = Counter(nums).most_common(1)[0][0]
        return most_common_value
        
