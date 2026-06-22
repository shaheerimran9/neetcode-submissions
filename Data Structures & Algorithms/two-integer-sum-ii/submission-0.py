class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array ints -> numbers
        # sorted: low to high
        # return -> indicies two nums -> sum to target (1 indexed)

        l, r = 0, len(numbers) - 1
        while l < r:
            # Check the sum of the two numbers
            pair_sum = numbers[l] + numbers[r]
            # Compare against the target
            if pair_sum == target:
                return [l+1, r+1]
            # pairs greater than target -> decrease
            elif pair_sum > target:
                r -= 1
            # pairs less than target -> increase
            elif pair_sum < target:
                l += 1