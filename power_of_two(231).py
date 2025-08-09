class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst=[]
        for i in range(-32,33):
            re=2**i
            lst.append(re)
        if n not in lst:
            return False
        else:
            return True

      # alternative answer above code has 4ms runtime
        return n>0 and not (n & (n-1)) # this line of code has 0ms runtime
