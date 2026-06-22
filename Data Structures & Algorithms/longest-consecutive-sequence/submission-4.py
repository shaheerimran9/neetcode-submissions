class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            nums_set.add(num)

        max_len = 0

        for num in nums:
            if num - 1 not in nums_set:
                curr_len = 1
                while num + curr_len in nums_set:
                    curr_len += 1
                max_len = max(curr_len, max_len)

        return max_len