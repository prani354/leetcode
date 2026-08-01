class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        flag = True
        
        ans = []
        for i in range(len(grid)):
            res = []
            if flag:
                for j in range(0,len(grid[0]),2):
                    res.append(grid[i][j])
                
                ans.extend(res)
                flag = False

            else:
                for j in range(1,len(grid[0]),2):
                    res.append(grid[i][j])
                
                ans.extend(res[::-1])
                flag = True
                

        return ans