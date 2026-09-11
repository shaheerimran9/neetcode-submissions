class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set()

        for num in nums:
            nums_set.add(num)

        for num in nums:
            if (num - 1) not in nums_set:
                seq = 1
                while (num + seq) in nums_set:
                    seq += 1
                longest = max(seq, longest)

        return longest

