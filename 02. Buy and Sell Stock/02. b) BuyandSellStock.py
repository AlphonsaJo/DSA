class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        profit_list = []
        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[:i])
            if profit > 0:
                profit_list.append(profit)
        
        return max(profit_list) if profit_list else 0
