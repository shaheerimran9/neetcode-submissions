class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # int array piles -> number bananas in each pile
        # int h -> number of hours to eat all bananas
        # return -> k: minimum banana/hr eating speed
        # time -> pile/speed(k)

        l, r = 1, max(piles)
        while l < r:
            speed = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/speed)
            if hours > h:
                l = speed + 1
            else:
                r = speed
        return r


                
