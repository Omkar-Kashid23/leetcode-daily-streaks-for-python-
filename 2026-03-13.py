class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        h = [(t, t, 1) for i, t in enumerate(workerTimes)]
        heapify(h)
        while mountainHeight > 1:
            ps, wt, x = heappop(h)
            heappush(h, (ps + wt * (x + 1), wt, x + 1))
            mountainHeight-= 1
        return heappop(h)[0] 
