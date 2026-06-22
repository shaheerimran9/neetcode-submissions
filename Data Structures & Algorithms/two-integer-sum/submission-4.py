class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input -> array of nums
        # Output -> Indicies of two numbers that == target & indicies not same

        # Loop through the numbers in the array
        # Calculate the complement (missing number)
        # Check if the complement is already in our hashmap
         # If it is return the indicies
        # Otherwise add the curent number to the hashmap

        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i