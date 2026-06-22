class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Input -> Array nums
        #Output -> Return triplets that == 0 and indicies are distinct
        #Note -> No duplicates allowed

        #We can sort the nums array to make it easier to find the target 0
        #Loop through each number
        #Use two pointers to find 2 more nums that == 0
        #If we find a triplet add to result and move the pointers
        #If the number is same as the prev number keep moving the pointers

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                if triplet > 0:
                    r -= 1
                elif triplet < 0:
                    l += 1
                elif triplet == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res