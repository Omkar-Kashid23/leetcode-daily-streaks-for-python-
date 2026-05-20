class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        cnt = 0
        for i in range(len(A)):
            re = len(set(A[:i+1]) & set(B[:i+1]))
            res.append(re)
        return res
