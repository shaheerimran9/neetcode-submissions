class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # mxn array matrix, int target
        # return -> true if target in matrix or False

        # Run binary search on the matrix rows
        # Find the mid
        # Check if the target lies between the mid row start - end
        # If midrow[0] > target: search above
        # If midrow[-1] < target: search below
        # return false if nothing returns
        def binary_search(row, target):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                elif row[mid] > target:
                    r = mid - 1
            return False

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                return binary_search(matrix[mid], target)
            elif matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
        return False