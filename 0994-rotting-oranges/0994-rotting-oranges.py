from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty = 0
        fresh = 1
        rotten = 2

        time = -1
        q = deque()
        num_fresh= 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == fresh:
                    num_fresh += 1

                elif grid[i][j] == rotten:
                    q.append((i,j))  #All rotten oranges are updated in the queue

        if num_fresh == 0: return 0

        while q:
            size = len(q)
            time += 1

            for _ in range(size):
                i,j = q.popleft()

                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        num_fresh -= 1   
                        q.append((r,c))

        if num_fresh == 0:
            return time

        return -1

            

