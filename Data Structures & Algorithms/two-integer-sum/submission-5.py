class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Input -> array nums, int target
        #Output -> Return indicies i, j where nums[i]+nums[j] == target
        #Note -> indicies i and j can't be the same

        # Approach 1: Requires 2 Passes
        # Map the numbers -> index in a hashmap
        # Loop through each number and find target - number in the hashmap
        # Return the indicies of the two numbers

        # Approach 2: Single Pass
        # Have a hashmap with number -> index
        # Loop through each number
        # Figure out the complement (target - number)
        # Check the hashmap to see if complement exists
        # If complement is in the hashmap -> Return indicies
        # If not add the current number to the hashmap and move on

        nums_map = {} #number -> index
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return [nums_map[complement], index]
            nums_map[num] = index