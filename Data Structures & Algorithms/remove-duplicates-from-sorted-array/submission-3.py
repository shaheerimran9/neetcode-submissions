class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 1
        while r < len(nums):
            #If r - 1 is the same as r:
                #We move r ahead
            #If it's not the same we nums[l] = nums[r]
            if nums[r - 1] == nums[r]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l