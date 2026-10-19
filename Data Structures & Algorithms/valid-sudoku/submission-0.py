# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # size = len(board)
        # corners = [(0,0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        # def checkSquare(corner):
        #     row, col = corner[0], corner[1]
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             elem = board[row + i][col + j]
        #             if not (elem.isdigit() or elem == ".") or elem in seen:
        #                 return False
        #             seen.add(elem)
        #     return True

        # def checkRow(corner):
        #     row = corner[0]
        #     seen = set()
        #     for col in range(size):
        #         elem = board[row][col]
        #         if not (elem.isdigit() or elem == ".") or elem in seen:
        #             return False
        #         seen.add(elem)
        #     return True

        # def checkCol(corner):
        #     col = corner[1]
        #     seen = set()
        #     for row in range(size):
        #         elem = board[row][col]
        #         if not (elem.isdigit() or elem == ".") or elem in seen:
        #             return False
        #         seen.add(elem)
        #     return True


        # for corner in corners:
        #     if not checkSquare or not checkRow or not checkCol:
        #         return False
        # return True
                
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Determine which 3x3 square we are in (0-8)
                # Formula: (row // 3) * 3 + (col // 3)
                square_idx = (r // 3) * 3 + (c // 3)

                # Check if value already exists in current row, col, or square
                if val in rows[r] or val in cols[c] or val in squares[square_idx]:
                    return False
                
                # Add value to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[square_idx].add(val)
                
        return True