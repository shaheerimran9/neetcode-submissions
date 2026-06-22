class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l, r = 0, 0
        while r < len(nums):
            if abs(r - l) > k:
                seen.remove(nums[l])
                l += 1
            elif nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
                r += 1
        return False