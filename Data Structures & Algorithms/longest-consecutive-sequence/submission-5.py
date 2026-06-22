class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Input -> array of integers nums
        #Return -> length of the longest consecutive sequence of elements

        #We want to check the max consecutive sequence of elements
        #To do that we need to find the start of a sequence
        #To find the start of a sequence the element before that shouldn't exist
        #We can use a set to track elements and check which exist

        #Have a set
        #Have a max_result variable
        #Loop through each number in nums and add it to the set
        #Loop through each number and check if num - 1 is in set
            #If its not in set -> Start of the sequence
            #If it's in the set -> continue
        #Use a curr_result variable
        #Loop till num + 1 not in set:
        #Increment curr_result
        #Set max_result to max of curr_result or max_result
        #Return max_result in the end

        numbers = set()
        max_result = (0)
        for num in nums:
            numbers.add(num)

        for num in nums:
            if num - 1 in numbers:
                continue
            curr_res = 1
            while num + 1 in numbers:
                curr_res += 1
                num += 1
            max_result = max(curr_res, max_result)
        return max_result


