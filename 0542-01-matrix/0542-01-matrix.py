from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        q = deque()

        seen = [[0 for _ in range(m)] for _ in range(n)]
        distance = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    seen[i][j] = 1

        while q:
            i,j,dist = q.popleft()
            distance[i][j] = dist

            for r,c in [(-1,0),(0,-1),(0,1),(1,0)]:
                new_i,new_j = i+r,j+c
                if 0 <= new_i < n and 0 <= new_j < m:
                    if seen[new_i][new_j] == 1:
                        continue
                    q.append((new_i,new_j,dist+1))
                    seen[new_i][new_j] = 1

        return distance