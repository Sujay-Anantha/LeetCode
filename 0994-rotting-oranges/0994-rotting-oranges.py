class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Queue to store rotten oranges
        queue = deque()
        fresh_oranges = 0
        
        # Step 1: Enqueue all initially rotten oranges and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # Rotten orange
                    queue.append((i, j, 0))  # (row, col, time elapsed)
                elif grid[i][j] == 1:  # Fresh orange
                    fresh_oranges += 1
        
        # Step 2: BFS to rot neighboring fresh oranges
        minutes = 0  # Keep track of the time (minutes)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        while queue:
            i, j, minutes = queue.popleft()
            
            # Visit all 4 possible neighbors
            for di, dj in directions:
                ni, nj = i + di, j + dj
                # Check if the new coordinates are valid and the orange is fresh
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    # Rot the fresh orange
                    grid[ni][nj] = 2
                    fresh_oranges -= 1  # Decrease count of fresh oranges
                    # Enqueue the newly rotten orange with incremented time
                    queue.append((ni, nj, minutes + 1))
        
        # Step 3: If there are still fresh oranges, return -1
        if fresh_oranges > 0:
            return -1
        
        # Step 4: Return the total minutes it took for all oranges to rot
        return minutes
