class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = 10**9

        # Bitmask per row: bit j is 1 iff grid[i][j] == 1
        rowmask = []
        for i in range(m):
            mask = 0
            for j in range(n):
                if grid[i][j]:
                    mask |= (1 << j)
            rowmask.append(mask)

        # Area of the tightest rectangle covering all 1s inside
        # rows [t..b] and cols [l..r] (inclusive). 0 if no 1s.
        def area_sub(t, b, l, r):
            if t > b or l > r:
                return 0
            mask_range = ((1 << (r - l + 1)) - 1) << l
            union = 0
            first_row = -1
            last_row = -1
            for i in range(t, b + 1):
                bits = rowmask[i] & mask_range
                if bits:
                    if first_row == -1:
                        first_row = i
                    last_row = i
                    union |= bits
            if first_row == -1:
                return 0
            min_col = (union & -union).bit_length() - 1
            max_col = union.bit_length() - 1
            return (last_row - first_row + 1) * (max_col - min_col + 1)

        # Precompute best 2-rectangle covers in a column-interval [l..r]
        twoRect_v = [[INF] * n for _ in range(n)]
        area_v = [[0] * n for _ in range(n)]
        for l in range(n):
            for r in range(l, n):
                area_v[l][r] = area_sub(0, m - 1, l, r)
                best = INF
                # Two vertical stripes inside [l..r]
                for k in range(l, r):
                    best = min(best,
                               area_sub(0, m - 1, l, k) + area_sub(0, m - 1, k + 1, r))
                # Two horizontal stripes inside [l..r]
                for s in range(0, m - 1):
                    best = min(best,
                               area_sub(0, s, l, r) + area_sub(s + 1, m - 1, l, r))
                if best == INF:
                    best = 0
                twoRect_v[l][r] = best

        # Precompute best 2-rectangle covers in a row-interval [t..b]
        twoRect_h = [[INF] * m for _ in range(m)]
        area_h = [[0] * m for _ in range(m)]
        for t in range(m):
            for b in range(t, m):
                area_h[t][b] = area_sub(t, b, 0, n - 1)
                best = INF
                # Two horizontal stripes inside [t..b]
                for s in range(t, b):
                    best = min(best,
                               area_sub(t, s, 0, n - 1) + area_sub(s + 1, b, 0, n - 1))
                # Two vertical stripes inside [t..b]
                for c in range(0, n - 1):
                    best = min(best,
                               area_sub(t, b, 0, c) + area_sub(t, b, c + 1, n - 1))
                if best == INF:
                    best = 0
                twoRect_h[t][b] = best

        # Best with 1 rectangle (just the global tight bounding box)
        best1 = area_sub(0, m - 1, 0, n - 1)

        # Best with 2 rectangles on the whole grid
        best2 = min(twoRect_v[0][n - 1], twoRect_h[0][m - 1])

        # Best with 3 rectangles:
        best3 = INF
        # (a) Three vertical stripes
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                s = (area_sub(0, m - 1, 0, i) +
                     area_sub(0, m - 1, i + 1, j) +
                     area_sub(0, m - 1, j + 1, n - 1))
                best3 = min(best3, s)
        # (b) Three horizontal stripes
        for i in range(m - 2):
            for j in range(i + 1, m - 1):
                s = (area_sub(0, i, 0, n - 1) +
                     area_sub(i + 1, j, 0, n - 1) +
                     area_sub(j + 1, m - 1, 0, n - 1))
                best3 = min(best3, s)
        # (c) T-splits: one side has 1 rect, the other side has best 2-rect cover
        for c in range(n - 1):  # vertical split
            best3 = min(best3,
                        area_sub(0, m - 1, 0, c) + twoRect_v[c + 1][n - 1],
                        twoRect_v[0][c] + area_sub(0, m - 1, c + 1, n - 1))
        for r in range(m - 1):  # horizontal split
            best3 = min(best3,
                        area_sub(0, r, 0, n - 1) + twoRect_h[r + 1][m - 1],
                        twoRect_h[0][r] + area_sub(r + 1, m - 1, 0, n - 1))

        # Using exactly 3 rectangles is never worse than using <= 2
        # (you can split a rectangle without increasing total area),
        # so final answer is the min across 1, 2, or 3 rectangles:
        return min(best1, best2, best3) 
