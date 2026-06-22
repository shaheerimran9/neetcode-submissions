class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array nums -> no dups -> sorted small to big, int target
        # search for target -> return its index or -1

        # Initialize two pointers, l & r
        # while l <= r
        # calculate the midpoint
        # compare the midpoint to the target
        # if the midpoint is less than the target -> move l
        # if the midpoint is greater than the target -> move r
        # if midpoint is = to target return midpoint (index)
        # return -1 if loop ends

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return -1