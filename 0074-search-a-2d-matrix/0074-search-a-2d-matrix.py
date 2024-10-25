class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        
        while l <= r:
            mid = (l + r) // 2
            # Convert the mid index back into a row and column
            row = mid // cols
            col = mid % cols
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
