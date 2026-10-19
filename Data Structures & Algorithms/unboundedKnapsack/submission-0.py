class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = {}

        def explore(i, capacity):
            if i == len(profit):
                return 0
            if capacity < 0:
                return 0
            
            # have we seen this before
            if (i, capacity) in dp:
                return dp[(i, capacity)]
            
            # otherwise we have 3 cases
            # we do not take the elem, and leave 
            choice3 = explore(i+1, capacity)

            # we take this element, and stay
            if capacity - weight[i] >= 0:
                choice1 = profit[i] + explore(i, capacity - weight[i])
                dp[(i, capacity)] = max(choice1, choice3)
            else:
                dp[(i, capacity)] = choice3
            
            return dp[(i, capacity)]
        return explore(0, capacity)

