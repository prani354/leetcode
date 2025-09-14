from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))

        res = 0

        while q:
            i , j = q.popleft()
            for r,c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_i , new_j = i+r , j+c
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0:
                    q.append((new_i,new_j))
                    grid[new_i][new_j] = grid[i][j] + 1
                    res = max(res,grid[new_i][new_j])

        return res-1

        