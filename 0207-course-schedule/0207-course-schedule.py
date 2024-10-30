from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list and in-degree array
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        
        # Step 2: Initialize queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_courses = 0
        
        # Step 3: Process courses in topological order
        while queue:
            course = queue.popleft()
            completed_courses += 1
            
            # Reduce in-degree of neighbors
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check if all courses are completed
        return completed_courses == numCourses
