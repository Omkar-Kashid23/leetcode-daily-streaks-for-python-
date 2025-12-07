class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lo = min(stations)
        hi = max(stations) * len(stations)+k

        stations = [0]*(r) + stations +[0]*r

        def check(med):
            available,ind=k,r
            window = sum(stations[:2*r])

            added = defaultdict(int)
            while ind<len(stations)-r:
                window += stations[ind+r]
                if window<med:
                    diff = med-window
                    if diff>available:return False
                    window += diff
                    added[ind + r]=diff
                    available -=diff
                window -= (stations[ind-r]+added[ind-r])
                ind += 1
            return True
        while lo<=hi:
            m = (lo+hi)//2
            if check(m):res,lo = m,m+1
            else:hi = m-1
        return res
