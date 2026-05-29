class Solution:
    def minElement(self, nums: List[int]) -> int:
        lst = []
        for i in nums:
            total = sum(int(digit) for digit in str(i))
            lst.append(total)
        return min(lst)
