class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        count=0
        # flag=0
        # buy=999999999999
        # sell=0
        
        for i in range(len(prices)-1):
            if (prices[i+1]-prices[i])>0:
                count+=prices[i+1]-prices[i]
        return count