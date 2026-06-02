class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def f(a,b,aa,bb):
            e= min(map(add,a,b))
            return min(max(s,e)+d for s,d in zip(aa,bb))
        return min(f(landStartTime,landDuration,waterStartTime,waterDuration),
                   f(waterStartTime,waterDuration,landStartTime,landDuration))
