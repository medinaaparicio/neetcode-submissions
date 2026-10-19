class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        # top down approach
        # dp = {}
        # def dfsmemo(row, col):
        #     if row == rows or col == cols:
        #         return 0
        #     if obstacleGrid[row][col] == 1:
        #         return 0
        #     if row == rows - 1 and col == cols - 1:
        #         return 1
            
        #     if (row, col) in dp:
        #         return dp[(row, col)]
            
        #     dp[(row, col)] = dfsmemo(row+1, col) + dfsmemo(row, col+1)
        #     return dp[(row, col)]
        # return dfsmemo(0, 0)

        # bottom up approach 
        prevRow = [0] * cols
        prevRow[-1] = 1
        for row in range(rows - 1, -1, -1):
            currRow = [0] * cols
            # only set the edge to 1 if it's not a 1
            if obstacleGrid[row][-1] != 1 and prevRow[-1] != 0:
                currRow[-1] = 1
            
            for col in range(cols-2, -1, -1):
                if obstacleGrid[row][col] != 1:
                    currRow[col] = currRow[col + 1] + prevRow[col]
            prevRow = currRow
        return prevRow[0]
