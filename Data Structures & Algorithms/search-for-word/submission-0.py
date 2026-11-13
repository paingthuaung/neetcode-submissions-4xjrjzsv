class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        
        def dfs(r, c, index):
            if index == len(word):
                return True
            
            if  r < 0 or r >= row or c < 0 or c >= col:
                return False
            
            if (r,c)  in visited:
                return False

            if board[r][c] != word[index]:
                return False

            visited.add((r,c))

            if dfs(r + 1, c, index + 1):
                return True
            if dfs(r - 1, c, index + 1):
                return True
            if dfs(r, c + 1, index + 1):
                return True
            if dfs(r, c - 1, index + 1):
                return True

            visited.remove((r,c))
            return False
        
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        
        return False

                
            


        