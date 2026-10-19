class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # 1. build transpose 
        rows, cols = len(matrix), len(matrix[0]) 
        t = [[0 for r in range(rows)] for c in range(cols)]
        for i in range(rows):
            for j in range(cols):
                t[j][i] = matrix[i][j]

        return t