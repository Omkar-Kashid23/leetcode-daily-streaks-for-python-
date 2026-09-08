class Solution:
    def countCommas(self, n: int) -> int:
        # if n < 1000:return 0
        # else:
        #     return n - 999
        return 0 if n < 1000 else n - 999
