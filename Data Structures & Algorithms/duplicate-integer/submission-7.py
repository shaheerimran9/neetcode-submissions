class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Input -> integer array nums
        #Output -> True if duplicate || False if no duplicates

        # Have a set
        # Loop through each number in array
        # Check if the number is in the set
        # If the number is in the set -> Return True (Duplicate Found)
        # Otherwise add the number to the set
        # Return False in the end (No Duplicate Found)

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


