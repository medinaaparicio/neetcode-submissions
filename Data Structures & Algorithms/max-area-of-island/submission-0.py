class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        biggest = 0

        def dfs(r, c):
            # out of bounds or blocked 
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 # mark as visited
            right = dfs(r, c+1)
            left = dfs(r, c-1)
            up = dfs(r-1, c)
            down = dfs(r+1, c)
            return 1 + right + up + left + down
        
        for r in range(ROWS):
            for c in range(COLS):
                area = dfs(r, c)
                biggest = max(biggest, area)
        return biggest