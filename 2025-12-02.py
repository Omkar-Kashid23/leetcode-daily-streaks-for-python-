class Fenwick:
    def __init__(self, n):
        self.n = n
        self.fw = [0] * (n + 1)

    def update(self, i, v):
        while i <= self.n:
            self.fw[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s

    def range(self, l, r):
        if r < l: 
            return 0
        return self.query(r) - self.query(l - 1)


class Solution:
    def countTrapezoids(self, points):
        MOD = 10**9 + 7

        # --- group points by y ---
        from collections import defaultdict
        by_y = defaultdict(list)
        for x, y in points:
            by_y[y].append(x)

        # --- coordinate compress all x ---
        xs = sorted({x for x, _ in points})
        comp = {x: i+1 for i, x in enumerate(xs)}  # Fenwick is 1-indexed
        M = len(xs)

        # Fenwick trees for:
        #   starts: counts of interval left endpoints
        #   ends:   counts of interval right endpoints
        start_ft = Fenwick(M)
        end_ft   = Fenwick(M)

        ans = 0

        # Process each y-level independently (order doesn't matter)
        for y, arr in by_y.items():
            arr.sort()
            k = len(arr)

            # First, compute overlaps with existing intervals:
            # We compressed intervals so each x_i contributes (k-i) starts
            # and each x_j contributes (j-1) ends.
            for i in range(k):
                xi = comp[arr[i]]
                starts_here = (k - 1 - i)  # intervals starting at arr[i]

                if starts_here == 0:
                    continue

                # for each start at xi, it pairs with ends j > i
                # but more simply: an interval from arr[i] needs all possible right endpoints:
                # for each potential right endpoint arr[j], j > i:
                # Instead of iterating j, observe:
                # ANY previous interval that overlaps ANY (xi,xj) is one where:
                #   previous_start <= xj-1
                #   previous_end   >= xi+1
                #
                # To compress this, we just iterate the j's:
                # Actually simpler: iterate j and accumulate.
                for j in range(i+1, k):
                    xj = comp[arr[j]]

                    # previous intervals that start ≤ xj-1
                    left_cnt = start_ft.query(xj - 1)

                    # previous intervals that end < xi
                    right_cnt = end_ft.query(xi - 1)

                    ans = (ans + (left_cnt - right_cnt)) % MOD

            # Now add this y-level's intervals into Fenwick trees
            # without inserting each pair (O(k), not O(k^2))
            for i in range(k):
                xi = comp[arr[i]]
                cnt_start = k - 1 - i   # how many intervals start at arr[i]
                if cnt_start > 0:
                    start_ft.update(xi, cnt_start)

                cnt_end = i  # arr[i] is right endpoint for i intervals
                if cnt_end > 0:
                    end_ft.update(xi, cnt_end)

        return ans % MOD

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        freq = Counter(y for _, y in points)
        
        total = 0      # sum(ai)
        total_sq = 0   # sum(ai^2)

        for f in freq.values():
            if f >= 2:
                a = f*(f-1)//2
                total += a
                total_sq += a*a

        total %= MOD
        total_sq %= MOD

        # formula: (S^2 - sum(a_i^2)) / 2
        ans = (total*total - total_sq) * pow(2, MOD-2, MOD)
        return ans % MOD


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        freq=Counter(p[1] for p in points)
        Sum, c2=0, 0
        for f in freq.values():
            if f<=1: continue
            c=f*(f-1)//2
            Sum+=c
            c2+=c*c
        return (Sum*Sum-c2)//2%(10**9+7)
        
