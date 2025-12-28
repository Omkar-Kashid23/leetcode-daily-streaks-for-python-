class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        r = 0             # Start at first row
        c = cols - 1      # Start at last column
        
        while r < rows and c >= 0:
            if grid[r][c] < 0:
                # If negative, all elements below it in this column are negative
                cnt += (rows - r)
                c -= 1    # Move to the previous column
            else:
                # If positive, move to the next row to find smaller numbers
                r += 1
        return cnt
