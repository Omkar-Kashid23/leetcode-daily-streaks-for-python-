class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        r, c = len(grid), len(grid[0])
        visited = [[0]*c for _ in range(r)]

        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = 1
        reached = False
        t = 0
        while not reached:
            while heap[0][0] <= t:
                # get neighbors
                height, i, j = heappop(heap)
                if i == r-1 and j == c-1:
                    reached = True
                    break
                for di,dj in directions:
                    ni, nj = i+di, j+dj
                    if 0<=ni<r and 0<=nj<c and not visited[ni][nj]:
                        heappush(heap, (grid[ni][nj], ni, nj))
                        visited[ni][nj] = 1
            t += 1
        
        return t-1
