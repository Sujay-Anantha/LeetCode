class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        
        for row in wall:
            position = 0
            # Ignore the last brick in each row because we cannot draw a line at the very end of the wall
            for brick in row[:-1]:
                position += brick
                edge_counts[position] += 1
        
        # Find the maximum number of edges that align
        max_edges = max(edge_counts.values(), default=0)
        
        # Minimum number of bricks crossed is the total number of rows minus the number of aligned edges
        return len(wall) - max_edges
        