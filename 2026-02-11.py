class LazySegmentTree:
    def __init__(self, n: int, arr: Optional[list[int]] = None):
        self.n = n
        self.mx = [0] * (n << 2)  # maximum value in segment
        self.mn = [0] * (n << 2)  # minimum value in segment
        self.tag = [0] * (n << 2) # lazy propagation tag
        self.arr = arr.copy() if arr else [0] * n
        if arr: self.build(1, 0, n)

    def merge(self, pos: int, s: int, t: int):
        self.mx[pos] = max(self.mx[pos << 1], self.mx[pos << 1 | 1])
        self.mn[pos] = min(self.mn[pos << 1], self.mn[pos << 1 | 1])

    def update(self, pos: int, s: int, t: int, val: int):
        self.mx[pos] += val
        self.mn[pos] += val
        self.tag[pos] += val

    def build(self, pos: int, s: int, t: int):
        if s + 1 == t:
            self.mx[pos] = self.arr[s]
            self.mn[pos] = self.arr[s]
            return
        mid = (s + t) >> 1
        self.build(pos << 1, s, mid)
        self.build(pos << 1 | 1, mid, t)
        self.merge(pos, s, t)

    def push(self, pos: int, s: int, t: int):
        if not self.tag[pos]: return
        mid = (s + t) >> 1
        self.update(pos << 1, s, mid, self.tag[pos])
        self.update(pos << 1 | 1, mid, t, self.tag[pos])
        self.tag[pos] = 0

    def query(self, pos: int, s: int, t: int, x: int) -> int:
        # find leftmost index with value == x
        if s + 1 == t: return s
        self.push(pos, s, t)
        mid = (s + t) >> 1
        if self.mn[pos << 1] <= x <= self.mx[pos << 1]:
            return self.query(pos << 1, s, mid, x)
        return self.query(pos << 1 | 1, mid, t, x)

    def modify(self, pos: int, s: int, t: int, qs: int, qt: int, val: int):
        if qt <= s or t <= qs: return
        if qs <= s and t <= qt:
            self.update(pos, s, t, val)
            return
        self.push(pos, s, t)
        mid = (s + t) >> 1
        self.modify(pos << 1, s, mid, qs, qt, val)
        self.modify(pos << 1 | 1, mid, t, qs, qt, val)
        self.merge(pos, s, t)

class Solution:
    def longestBalanced(self, l: List[int]) -> int:
        n = len(l) + 1
        last = {}                  # last occurrence of each value
        seg = LazySegmentTree(n)
        ans = cur = 0

        for i, v in enumerate(l, 1):
            x = 1 if v & 1 else -1      # odd +1, even -1
            if pi := last.get(v):
                cur -= x
                seg.modify(1, 0, n, pi, n, -x)  # remove previous effect
            cur += x
            seg.modify(1, 0, n, i, n, x)        # add current effect
            last[v] = i
            ans = max(ans, i - seg.query(1, 0, n, cur))  # query leftmost index

        return ans
