class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        count = 0

        def magic(r,c):
            s = set()

            for i in range(3):
                for j in range(3):

                    if grid[r+i][c+j] > 9 or grid[r+i][c+j] < 1:
                        return False

                    s.add(grid[r+i][c+j])

            if len(s) != 9:
                return False

            #rows check

            for i in range(3):
                if sum(grid[r+i][c+c2] for c2 in range(3)) != 15: return False

            #cols check

            for j in range(3):
                if sum(grid[r+r2][c+j] for r2 in range(3)) != 15: return False

            #diagonal check

            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False

            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False

            return True

        for i in range(rows-2):
            for j in range(cols-2):
                if magic(i,j):
                    count += 1


        return count



                    