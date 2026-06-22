class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Input -> Array heights that represents height of a bar
        #Output -> Return maximum amount of water that can be stored
        #Note -> Area = Length(height) * Width

        #We basically need to find the maximum area
        #Use two pointers at the start and end
        #Calculate the current area
        #Update max_area
        #Move the pointer with the lower height (to possibly increase area)

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
