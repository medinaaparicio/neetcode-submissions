class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0: return 0

        ch1, ch2 = text1[0], text2[0]
        # make the board (later we can space optimize)
        rows, cols = len(text1), len(text2)
        board = [[0] * (cols + 1) for i in range(rows + 1)]

        # # fill top row and left col
        # count = 0
        # for col in range(cols):
        #     if ch1 == text2[col]:
        #         count += 1
        #     board[0][col] = min(count, 1)
        
        # count = 0
        # for row in range(rows):
        #     if ch2 == text1[row]:
        #         count += 1
        #     board[row][0] = min(count, 1)

        # fill up the rest of the board
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if text1[row-1] == text2[col-1]:
                    board[row][col] = board[row-1][col-1] + 1
                else:
                    board[row][col] = max(board[row-1][col], board[row][col-1])
        return board[-1][-1]