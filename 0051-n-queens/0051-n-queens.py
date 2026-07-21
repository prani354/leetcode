class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isSafe(r,c):
            n = len(board)
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                if r - i >= 0 and c - i >= 0 and board[r-i][c-i] == 'Q':
                    return False
                if r - i >= 0 and c + i < n and board[r-i][c+i] == 'Q':
                    return False
            return True

        def solve(r):
            if r == n: # Base case
                res.append(["".join(b) for b in board])
                return
            for c in range(0,n):
                if isSafe(r,c):
                    # Recursive Backtracking
                    board[r][c] = 'Q'
                    solve(r+1)
                    board[r][c] = '.' #popping if not matched



        board = [['.'] * n for _ in range(n)]
        
        res = []
        solve(0)
        return res