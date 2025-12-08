class Solution:
    def countTriples(self, n: int) -> int:
        if n<=4:
            return 0
        sq = [i*i for i in range(n+1)]
        div = [0] + [n// i for i in range(1,n+1)]
        ans = 0
        i = 2
        while sq[i]<n:
            for j in range(1,n,2):
                if math.gcd(i,j)>1:
                    continue
                tot = sq[i]+sq[j]
                if tot>n:break
                ans += div[tot]
            i += 2
        return ans *2