class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col = len(grid[0])
        row = len(grid)
        num_island = 0
        def dfs(r, c):
            # base case
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            
            # mark as visited
            grid[r][c] = '0'            
            

            # explore all direction
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    num_island += 1
                    dfs(r, c)
        
        return num_island
            



        