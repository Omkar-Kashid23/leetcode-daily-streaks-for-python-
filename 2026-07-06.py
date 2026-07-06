class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        return sum(sum(ll<=l<r<=rr for ll,rr in intervals)==1 for l,r in intervals)
