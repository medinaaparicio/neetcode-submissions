class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # to solve this we can either do top down or bottom up
        # i will try to get more practice bottom up 

        prevRow = [0] * n # this creates our bottom row [0, 0, ..., 0]

        # starting at the bottom row, and moving upward
        for row in range(m -1, -1, -1):
            # we know to get to the final place we'll need to go upward and left
            # this is where your base case translates
            # you set it up yourself 

            # this is the one we are about to calculate
            currRow = [0] * n
            currRow[-1] = 1 # we've set our base case (left col to 1)

            # let's start moving left
            for col in range(n - 2, -1, -1):
                currRow[col] = prevRow[col] + currRow[col + 1]
            prevRow = currRow
        return prevRow[0]
            