class Solution:
    def minimumPushes(self, s: str) -> int:
        return sum(i//8+1 for i in range(len(s)))
