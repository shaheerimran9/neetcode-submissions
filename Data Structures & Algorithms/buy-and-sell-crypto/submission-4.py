class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        b, s = 0, 1

        while s < len(prices):
            #Not Profitable
            if prices[b] > prices[s]:
                b = s
            #Profitable
            else:
                profit = prices[s] - prices[b]
                maxProfit = max(profit, maxProfit)
            s += 1
        return maxProfit


