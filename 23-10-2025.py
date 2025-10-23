class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        if n <= 3:
            return s[0] == s[-1]

        v1 = v2 = 0
        c = 1
        s_int = [ord(ch) - 48 for ch in s]  # 5–10x faster than int() calls

        # precompute once
        n1 = n - 1
        for i in range(n):
            v1 += s_int[i] * c
            v2 += s_int[n1 - i] * c
            c = c * (n1 - 2 - i) // (i + 1)

        return (v1 - v2) % 10 == 0



            
