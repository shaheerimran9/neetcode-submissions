class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # int array piles -> number bananas in each pile
        # int h -> number of hours to eat all bananas
        # return -> k: minimum banana/hr eating speed
        # time -> pile/speed(k)

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil((p/k))
            if hours_needed > h:
                l = k + 1
            elif hours_needed <= h:
                res = k
                r = k - 1
        return res


                
