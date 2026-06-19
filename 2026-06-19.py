class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        lst = [0]
        n = len(gain)
        for i in range(n):
            lst.append(lst[i] + gain[i])
        return max(lst)