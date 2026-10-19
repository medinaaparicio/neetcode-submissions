class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # I'm going to divide this in two steps

        # finding the right row to traverse 
        # (by going through the first elements of the columns)

        # initialize, the c should be an r but my bad

        lc, rc = 0, len(matrix) - 1
        while lc <= rc:
            mc = lc + (rc - lc) // 2

            if target == matrix[mc][0]:
                return True 
            elif target > matrix[mc][0]:
                if target <= matrix[mc][-1]:
                    break # found right row
                lc = mc + 1
                
                # not plus one bc it could still be in that row 
            elif target < matrix[mc][0]:
                rc = mc - 1

        
        # here we should have the right row
        row = matrix[mc]
        l, r = 0, len(row) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target == row[m]:
                return True
            elif target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
        return False





        # finding the right element in the row 
