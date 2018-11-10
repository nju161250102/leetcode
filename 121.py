class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        bp = 0
        sp = 0
        profit = 0
        prices.append(prices[-1])
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                if prices[i] - prices[bp] > profit:
                    profit = prices[i] - prices[bp]
                    sp = i
            elif prices[i] < prices[i-1] and prices[i] <= prices[i+1]:
                if prices[i] < prices[bp]:
                    bp = i
        profit = max(profit, prices[-1] - prices[bp])
        return profit
