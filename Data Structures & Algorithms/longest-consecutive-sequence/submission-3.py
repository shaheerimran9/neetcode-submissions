class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Input -> Array integers: nums
        # Output -> Length of longest consecutive sequence
            # Ex. 1,2,3,4
            # Note: Elements DO NOT have to be in consecutive order in array
        
        # Find the starting of a sequence
            # A num is start of a sequence IF num - 1 does not exist
        
        # Add all nums to a set to check in O(1) time
        # Initialize max_len

        # Loop through each element in set -> Avoid array duplicates
            # If num - 1 not in set: Then its the start of a sequence
                # length = 1
                # While num + 1 in set: 
                    # Length += 1
                # max_len = max(length, max_len)
        # Return max_len

        nums_set = set()
        max_len = 0

        for num in nums:
            nums_set.add(num)
        
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_len = 1
                while num + curr_len in nums_set:
                    curr_len += 1
                max_len = max(curr_len, max_len)
        return max_len

