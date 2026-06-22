class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array -> nums
        # int -> target
        # return -> indicies i & j that equal target & i != j

        # for each number -> looking for target - num (2nd num)

        # value -> index
        map = {}

        for i, num in enumerate(nums):
            # Get the difference (2nd num)
            diff = target - num
            # Check if difference is in the map
            if diff in map:
                # Return indicies
                return [map[diff], i]
            # Add the current num to the map
            map[num] = i