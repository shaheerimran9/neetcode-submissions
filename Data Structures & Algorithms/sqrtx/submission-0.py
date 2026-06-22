class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if math.floor(mid ** 2) == x:
                return mid
            elif math.floor(mid ** 2) > x:
                r = mid - 1
            else:
                l = mid + 1
        return r             