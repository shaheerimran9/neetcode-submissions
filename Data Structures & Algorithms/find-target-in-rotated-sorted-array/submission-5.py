class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Need to figure out what sorted portion we are in
        #Check whether target lies in the sorted portion

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            #Midpoint == target
            if nums[mid] == target:
                return mid
            #Left sorted portion
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            #Right sorted portion
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1