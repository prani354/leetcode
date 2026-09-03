from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] == 1:
            return -1

        q = deque() # i,j,dist
        q.append((0,0,1))
        seen = {(0,0)} # visited index
        directions = [(1,0),(0,1),(0,-1),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]

        while q:
            i,j,dist = q.popleft()
            if i == n-1 and j == m-1:
                return dist
            for r,c in directions:
                new_i , new_j = i+r, j+c
                
                if 0 <= new_i < n and 0 <= new_j < m and  grid[new_i][new_j] == 0 and (new_i,new_j) not in seen:
                    seen.add((new_i,new_j))
                    q.append((new_i,new_j,dist+1))

        return -1


                

        

