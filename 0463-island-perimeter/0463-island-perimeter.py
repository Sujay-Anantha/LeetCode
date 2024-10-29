from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        def dfs(row, col):
            nonlocal perimeter
            # Check if out-of-bounds or water cell
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                perimeter += 1  # Each edge of water or boundary adds to perimeter
                return
            if grid[row][col] == 2:
                return  # Already visited cell, no contribution to perimeter
            
            # Mark the cell as visited
            grid[row][col] = 2
            
            # Check each direction
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left

        # Start DFS from the first land cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter  # Exit after finding the first island cell

        return perimeter
