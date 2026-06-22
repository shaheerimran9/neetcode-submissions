class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Input -> Array Prices
        #Output -> Int maxProfit
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            #If r is less than l that means we found lower price
            #Move l = r
            if prices[r] < prices[l]:
                l = r
            else:
                #If r is greater than l that means we can make profit
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
                r += 1
        return maxProfit