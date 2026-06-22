class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # int array -> heights
        # return -> max water container can store
        
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            # Check the area
            length, width = min(heights[l], heights[r]), r - l
            area = length * width
            # Check max between current area and stored max
            max_area = max(area, max_area)
            # Move the pointers based on the shorter height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area