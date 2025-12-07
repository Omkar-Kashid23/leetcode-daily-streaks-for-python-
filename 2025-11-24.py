from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        prefix = 0
        for bit in nums:
            prefix = (prefix * 2 + bit) % 5
            res.append(prefix == 0)
        return res
