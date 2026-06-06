class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        COLS = len(matrix[0])
        total_elements = len(matrix) * COLS
        
        def binarySearch(low, high):
            # base case: 
            if high < low:
                return False

            mid = low + (high - low) // 2
            mr = mid // COLS
            mc = mid % COLS

            if matrix[mr][mc] == target:
                return True

            # recursive case(s):
            if matrix[mr][mc] < target:
                return binarySearch(mid + 1, high)
            return binarySearch(low, mid - 1)

        # start in the middle row, middle element
        # recursively call binarySearch
        return binarySearch(0, total_elements - 1)

