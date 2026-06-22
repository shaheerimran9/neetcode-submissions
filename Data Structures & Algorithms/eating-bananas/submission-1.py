class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # int array piles -> number bananas in each pile
        # int h -> number of hours to eat all bananas
        # return -> k: minimum banana/hr eating speed

        # each hour -> choose a pile, eat k bananas
        # can't eat more than k bananas per hour

        # pile/speed = hours for that specific pile
        # total the hours and compare against h
        # piles = [1, 4, 3, 2] h = 9

        # Naive solution
        # Our speed k is what we need to test
        # Max we should need to eat is the biggest pile of banans

        # for i in range(1, max(piles) + 1):
        #     total_hours = 0
        #     for p in piles:
        #         total_hours += math.ceil((p/i))
        #     if total_hours <= h:
        #         return i

        # Sorted -> Binary Search
        # Have a k variable set to inf
        # find a mid point -> that's our k speed
        # Calc total hours for the piles
        # If total hours is less than or = h
        # update k to current mid or k && move r
        # if total hours is greater than h -> move left
        k = float('inf')
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            total_hours = 0
            for p in piles:
                total_hours += math.ceil((p/mid))
            if total_hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k
                
