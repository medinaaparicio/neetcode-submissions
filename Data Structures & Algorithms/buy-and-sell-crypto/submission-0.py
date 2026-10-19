class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        # return max profit
        profit, l = 0, 0

        for r in range(1, len(prices)):
            while prices[r] - prices[l] < 0:
                l += 1
            profit = max(profit, prices[r] - prices[l])
        return profit
                

        

# prices = [10,1,5,6,7,1]
#              l
#                       r

# prices = [10,8,7,5,2]
#                  l
#                    r