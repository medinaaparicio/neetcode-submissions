class Solution:
    def timeTaken(self, piles: List[int], m: int) -> int:
        count = 0
        for pile in piles:
            count = count + -(-pile // m)
        return count

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles)
        soFar = top 

        l, r = 1, top

        while l <= r:
            m = l + (r - l) // 2
            count = self.timeTaken(piles, m)

            if count <= h:
                soFar = m
                r = m - 1
            elif count > h:
                l = m + 1
        return soFar
        


        