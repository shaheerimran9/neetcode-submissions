class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # array ints -> numbers
        # sorted: low to high
        # return -> indicies two nums -> sum to target (1 indexed)

        l, r = 0, len(numbers) -1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            elif total > target:
                r -= 1