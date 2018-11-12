class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        bp = 0
        result = 0
        
        for i in range(1, len(prices)-1):
            if prices[i-1] < prices[i] and prices[i+1] <= prices[i]:
                result += (prices[i] - prices[bp])
                bp = None
            elif prices[i-1] >= prices[i] and prices[i+1] > prices[i]:
                bp = i
        
        if bp is not None and prices[-1] > prices[bp]:
            result += (prices[-1] - prices[bp])
        return result