class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0

        for r in range(1, len(prices)):          
            # Is the transaction profitable?
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(currentProfit, maxProfit)
            else:
                l = r
        return maxProfit
            