class Solution(object):
    def countSquares(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cou=1 if mat[0][0]==1 else 0
        m,n=len(mat),len(mat[0])
        for i in range(1,m):
            if mat[i][0]:
                cou+=1
        for i in range(1,n):
            if mat[0][i]:
                cou+=1
        
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j]==1:
                    mat[i][j]=min(mat[i-1][j-1],mat[i-1][j],mat[i][j-1])+1
                    cou+=mat[i][j]
      
        return cou
        
