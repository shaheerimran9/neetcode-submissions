class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Input -> int arr nums
        # Output -> True if duplicates || False if no duplicates

        # set -> track seen numbers
        # loop through nums
        # if num is in set -> DUPLICATE -> return True
        # otherwise add the num to the set
        # After finishing the loop return False

        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False