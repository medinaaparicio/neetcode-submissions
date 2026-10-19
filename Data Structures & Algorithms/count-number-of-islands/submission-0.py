class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dimensions
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            # out of bounds or blocked 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return 
            
            # set as visited
            grid[r][c] = "0"
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)
            return 
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands+= 1
        return islands