class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        m,n  = len(grid),len(grid[0])
        row = [0]*m
        for i in range(m):row[i] = next((j for j in reversed(range(n))if grid[i][j]),0) 
        ans = 0
        for k in range(m):
            for i,v in enumerate(row):
                if v<= k:
                    ans += i
                    row.pop(i)
                    break
            else:return -1
        return ans
