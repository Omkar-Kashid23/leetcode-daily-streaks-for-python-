class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ans,crow,occ = 0,1,1
        for r,s in sorted(reservedSeats) + [[n,10]]:
            if r > crow:ans += (r-crow-1)*2 +max(0, (9-occ)//4);  occ = 1
            if s>occ:ans += (s - occ -1)//4
            crow,occ = r,s|1
        return ans
