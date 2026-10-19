class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1. define pointers
        L, R = 0, len(heights) - 1
        best = 0

        while L < R:
            # 2. calculate best area
            area = (R - L) * min(heights[L], heights[R])
            best = max(best, area)

            # 3. shift up the one pointing to the lowest height
            if heights[L] < heights[R]:
                L+= 1
            else:
                R -= 1
        return best
        