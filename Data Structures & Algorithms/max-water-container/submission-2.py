class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Input -> int array heights
        # Return -> max amount of water that can be stored AKA max area

        max_area = 0
        # Area = L * W
        l, r = 0, len(heights)-1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area