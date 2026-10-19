class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def explore(i, target):
            if target == 0:
                return 0
            if i == len(coins):
                return float("inf")
            
            if (i, target) in dp:
                return dp[(i, target)]
            
            # otherwise tenemos dos casos
            balance = explore(i+1, target)
            new_amount = target - coins[i]
            if new_amount >= 0:
                include = 1 + explore(i, new_amount)
                balance = min(balance, include)
            
            dp[(i, target)] = balance
            return dp[(i, target)]

        res = explore(0, amount)
        if res == float("inf"):
            return -1
        return res
        