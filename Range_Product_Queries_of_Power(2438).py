<<<<<<< HEAD
MOD = 10**9 + 7

=======
>>>>>>> 163ad7b648ffdac927109e2d44b7eb9272981358
class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lst=[]
        while n>0:
            m=1
            while n >= (m<<1):
                m<<=1
            lst.append(m)
            n -= m
        lst.sort()
<<<<<<< HEAD
        dp=[[0]*k for _ in range(k)]
=======
        k=len(lst)
        MOD=10**9+7
>>>>>>> 163ad7b648ffdac927109e2d44b7eb9272981358
        dp=[[0]*k for  _ in range(k)]
        for i in range(k):
            dp[i][i]=lst[i]
        for i in range(k):
            for j in range(i+1,k):
                dp[i][j]=(dp[i][j-1]*lst[j])%MOD
        ans=[]
        for a,b in queries:
            ans.append(dp[a][b])
<<<<<<< HEAD
        return ans
=======
        return ans
>>>>>>> 163ad7b648ffdac927109e2d44b7eb9272981358
