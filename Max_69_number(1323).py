class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        three=(0,3,30,300,3000)
        a,n,d=-1,num,0
        while n>0:
            n,r=divmod(n,10)
            if r==6:
                a=d
            d+=1
        return num+three[a+1]
      # this is the alternative code
        n_str=str(num)
        n_str=n_str.replace('6','9',1)
        return int(n_str)
