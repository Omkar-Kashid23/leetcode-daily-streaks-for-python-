class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:return 0
        return (int(str(n).replace("0", ""))) * sum(int(i) for i in str(n)if int(i) != 0)
