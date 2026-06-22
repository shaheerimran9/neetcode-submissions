class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buy = 0, 0

        for sell in range(1, len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                currentProfit = prices[sell] - prices[buy]
                maxProfit = max(maxProfit, currentProfit)
        return maxProfit