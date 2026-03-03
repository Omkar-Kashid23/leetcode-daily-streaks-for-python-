class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        lst = []
        def rec(n):
            if n == 1:
                return "0"
            prev = rec(n-1)
            mapping = str.maketrans({"0":"1","1":"0"})
            inverted = prev.translate(mapping)
            rev = inverted[::-1]
            return prev + "1" + rev
        final = rec(n)
        return final[k-1]
