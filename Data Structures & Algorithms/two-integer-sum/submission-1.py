class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Input ->  arr of nums, int target
        #Output -> [i, j] where nums[i] + nums[j] == int target
        #* i != j

        nums_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums_map:
                return [nums_map[complement], index]
            else:
                nums_map[num] = index 
