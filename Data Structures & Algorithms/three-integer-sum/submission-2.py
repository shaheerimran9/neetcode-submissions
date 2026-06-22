class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize result
        res = []
        # If less than 3 nums -> can't be any triplet
        if len(nums) < 3:
            return res
        # Sort nums
        nums.sort()
        # If first num is positive -> can't sum to 0 -> only increases
        if nums[0] > 0:
            return res
        
        # Loop through nums with fixed i
        for i in range(len(nums)):
            # If not first num & num equals the one before it skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Initialize pointers    
            l, r = i + 1, len(nums) - 1

            while l < r:
                triplet = nums[i] + nums[l] + nums[r]
                # 3 cases
                if triplet < 0:
                    l += 1
                elif triplet > 0:
                    r -= 1
                else:
                    # Append triplet and move pointers
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Make sure we're not at duplicate l and r nums
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return res  