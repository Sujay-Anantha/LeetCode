class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        def is_white(coordinate: str) -> bool:
            column, row = coordinate[0], coordinate[1]
            # Convert column to a number (a=1, b=2, ..., h=8)
            col_num = ord(column) - ord('a') + 1
            row_num = int(row)
            # Return True if the sum of col_num and row_num is even (white), False if odd (black)
            return (col_num + row_num) % 2 == 0
        
        # Check if both coordinates have the same color
        return is_white(coordinate1) == is_white(coordinate2)