from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int):
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        min_damage = [[float("inf")] * cols for _ in range(rows)]
        min_damage[0][0] = grid[0][0]

        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if 0 <= next_row < rows and 0 <= next_col < cols:
                    damage = min_damage[row][col] + grid[next_row][next_col]

                    if damage < min_damage[next_row][next_col]:
                        min_damage[next_row][next_col] = damage

                        if grid[next_row][next_col] == 0:
                            queue.appendleft((next_row, next_col))
                        else:
                            queue.append((next_row, next_col))

        return min_damage[-1][-1] < health
