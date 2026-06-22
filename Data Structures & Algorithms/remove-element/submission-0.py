class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Input ->  arr nums, int val
        #Output -> int number of elements without int val

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k