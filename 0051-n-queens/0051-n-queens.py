class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
                return
            for col in range(n):
                if col in columns or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Place the queen
                board[row][col] = 'Q'
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Remove the queen (backtrack)
                board[row][col] = '.'
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        columns = set()  # Tracks which columns are occupied
        diag1 = set()    # Tracks occupied top-left to bottom-right diagonals (row - col)
        diag2 = set()    # Tracks occupied top-right to bottom-left diagonals (row + col)
        
        backtrack(0)
        return result