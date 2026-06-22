class Solution:
    def search(self, nums: List[int], target: int) -> int:

         # Set l, r boundaries
         # get mid
         # case 1: nums[l] <= nums[mid] MEANS LEFT SORTED PORTION
            # if target >= nums[l] and target <= nums[mid] -> move r
            # else: move l -> because its not on this side
         # case 2: nums[mid] <= nums[r] MEANS RIGHT SORTED PORTION
            # if target >= nums[mid] and target <= nums[r] -> 

        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid

            # Left Sorted Portion
            elif nums[l] <= nums[mid]:
                # Is the target in this range?
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right Sorted Portion
            else:
                # Is the target in this range?
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1