class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        flag = True
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            curr = []
            if flag == True:
                for j in range(0,m,2):
                    curr.append(grid[i][j])
                res.extend(curr)
                flag = False
            else:
                for j in range(1,m,2):
                    curr.append(grid[i][j])
                res.extend(curr[::-1])
                flag = True

        return res
        