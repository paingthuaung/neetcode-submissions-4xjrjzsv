class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        def isSafe(row,col):
            for r in range(row):
                for c in range(n):
                    if board[r][c] == 'Q':
                        # check if new queen conflict existing queen
                        if c == col:
                            return False
                        
                        if r - c == row  - col:
                            return False
                        
                        if r + c == row + col:
                            return False
            return True
            
        
        def backtrack(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'

                    backtrack(row + 1)

                    board[row][col] = '.'
        
        backtrack(0)
        return res


                
                    


        