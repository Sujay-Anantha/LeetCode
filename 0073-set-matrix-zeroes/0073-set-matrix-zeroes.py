class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height, width = len(matrix), len(matrix[0])

        # Record whether there is a 0 in the first row or column.
        firstRow0 = any(matrix[0][col] == 0 for col in range(width))
        firstCol0 = any(matrix[row][0] == 0 for row in range(height))

        # Iterate over rest of array, marking rows and columns with 0s.
        for r in range(1, height):
            for c in range(1, width):
                if matrix[r][c] == 0:
                    matrix[0][c] = matrix[r][0] = 0

        # Zero out rows whose first column is 0.
        for r in range(1, height):
            if matrix[r][0] == 0:
                for c in range(width):
                    matrix[r][c] = 0

        # Zero out columns whose first row is 0.
        for c in range(1, width):
            if matrix[0][c] == 0:
                for r in range(height):
                    matrix[r][c] = 0

        # Account for zeroes in first column.
        if firstCol0:
            for r in range(height):
                matrix[r][0] = 0

        # Account for zeroes in first row.
        if firstRow0:
            for c in range(width):
                matrix[0][c] = 0
        