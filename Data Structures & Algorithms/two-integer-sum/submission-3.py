class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Input -> array of nums
        # Output -> Indicies of two numbers that == target & indicies not same

        # Loop through the whole array of nums and add it to a hashmap
         # num : index
        # Loop again through nums and check if target - num is in hashmap
        # Need to make sure that the index of target - num != index of num

        indicies_map = {}
        for i, n in enumerate(nums):
            indicies_map[n] = i
        
        for i, n in enumerate(nums):
            complement = target - n
            if complement in indicies_map and indicies_map[complement] != i:
                return [i, indicies_map[complement]]