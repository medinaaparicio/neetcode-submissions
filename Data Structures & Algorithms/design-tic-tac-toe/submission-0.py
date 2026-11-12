class TicTacToe:

    def __init__(self, n: int):
        self.rows = [[0, 0] for _ in range(n)]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag = [[0, 0] for _ in range(2)] 
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if col == row:self.diag[0][player - 1] += 1
        if col + row == self.n - 1: self.diag[1][player - 1] += 1
        self.rows[row][player - 1] += 1
        self.cols[col][player - 1] += 1

        return 0 if (self.rows[row][player - 1] < self.n and self.cols[col][player - 1] < self.n and self.diag[0][player-1] < self.n and self.diag[1][player-1] < self.n) else player


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
