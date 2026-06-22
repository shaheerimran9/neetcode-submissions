class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy, sell = 0, 1

        for _ in range(1, len(prices)):
            #profitable?
            if prices[buy] < prices[sell]:
                currProfit = prices[sell] - prices[buy]
                maxProfit = max(currProfit, maxProfit)
            else:
                buy = sell
            sell += 1
        return maxProfit