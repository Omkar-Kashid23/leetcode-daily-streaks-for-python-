class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(S) == 3:return 1
        n = len(s)
        cnt = [0] * 3
        l = 0
        r = 0
        for i in range(n):
            cnt[ord(s[i]) - ord('a')] += 1
            while cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0:
                r += n - i
                cnt[ord(s[l]) - ord('a')] -= 1
                l += 1
        return r
