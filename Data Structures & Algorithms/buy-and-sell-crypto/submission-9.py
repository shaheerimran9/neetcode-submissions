class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Input -> Array prices
        #Output -> Return max profit

        #Buy on one day, sell on a different day in future
        #Buy low, sell high

        #We can use two pointers to track the prices
        #left is the buying, right is the selling
        #Go through the prices array
        #Check if it's profitable r - l
        #Update max profit
        #If it's not profitable then move l = r because found a lower price

        res = 0
        l = 0
        
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
        return res