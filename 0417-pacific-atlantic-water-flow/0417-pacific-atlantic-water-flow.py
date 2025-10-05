class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(cell,visited):
            if cell in visited:
                return

            visited.add(cell)
            r,c = cell
            
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs((nr,nc),visited)

        rows,cols = len(heights),len(heights[0])
        p , a = set() , set()

        #for edges cum intercells
        for r in range(rows):   #Left and right edges
            dfs((r,0),p)
            dfs((r,cols-1),a) 

        for c in range(cols):   #Top and bottom edges
            dfs((0,c),p)
            dfs((rows-1,c),a)

        return list(p&a)