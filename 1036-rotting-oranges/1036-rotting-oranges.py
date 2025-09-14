from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty,fresh,rotten = 0,1,2
        n = len(grid)
        m = len(grid[0])

        q = deque() 
        num_fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == fresh:
                    num_fresh += 1
                if grid[i][j] == rotten:
                    q.append((i,j))

        if num_fresh == 0:
            return 0

        time = -1

        while q:
            q_size = len(q)
            time += 1

            for _ in range(q_size):
                i,j = q.popleft()

                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        q.append((r,c))
                        num_fresh -= 1

        if num_fresh == 0:
            return time
        else:
            return -1
        