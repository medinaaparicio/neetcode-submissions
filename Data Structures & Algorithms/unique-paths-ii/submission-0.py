class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}
        def dfsmemo(row, col):
            if row == rows or col == cols:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == rows - 1 and col == cols - 1:
                return 1
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            dp[(row, col)] = dfsmemo(row+1, col) + dfsmemo(row, col+1)
            return dp[(row, col)]
        return dfsmemo(0, 0)