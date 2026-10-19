class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.pref = [[0] * COLS for _ in range(ROWS)]

        # 1. build prefix matrix
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 and col == 0: 
                    self.pref[row][col] = matrix[row][col]
                elif row == 0:
                    self.pref[row][col] = self.pref[row][col - 1] + matrix[row][col]
                elif col == 0:
                    self.pref[row][col] = self.pref[row-1][col] + matrix[row][col]
                else:
                    self.pref[row][col] = self.pref[row-1][col] + self.pref[row][col-1] - self.pref[row-1][col-1] + matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 2. get complete value
        total = self.pref[row2][col2]

        # 3. cut off excess
        if row1 != 0:
            total -= self.pref[row1 - 1][col2]
        if col1 != 0:
            total -= self.pref[row2][col1-1]
            if row1 != 0:
                total += self.pref[row1 - 1][col1 - 1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)