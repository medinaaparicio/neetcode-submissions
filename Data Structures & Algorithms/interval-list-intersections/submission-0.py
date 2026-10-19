class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        firstList = [[0,2],[5,10],[13,23],[24,25]], 
        secondList = [[1,5],[8,12],[15,24],[25,26]]
    

        """
        tracker1 = tracker2 = 0
        res = []
        while tracker1 < len(firstList) and tracker2 < len(secondList):
            s1, e1 = firstList[tracker1]
            s2, e2 = secondList[tracker2]
            start, end = max(s1, s2), min(e1, e2)

            # move the one that ended earliest
            if start <= end:
                res.append([start, end])

            if e1 < e2:
                tracker1 += 1
            else:
                tracker2 += 1
        return res

