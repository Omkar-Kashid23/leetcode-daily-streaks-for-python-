class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        if len(set(s)) == 1:return 2
        ans = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):
                char = s[j]
                if char not in freq:
                    freq[char] = 0
                freq[char] += 1
                if freq[char] > 2:
                    break
                ans = max(ans,j-i+1)
        return ans
