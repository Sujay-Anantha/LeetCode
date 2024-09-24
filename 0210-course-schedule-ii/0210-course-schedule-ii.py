class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
         # Step 1: Build the graph and compute indegrees
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # Directed edge from prereq to course
            indegree[course] += 1  # Increment indegree of the course
        
        # Step 2: Use a queue to perform topological sorting (BFS)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        topo_order = []
        
        while queue:
            course = queue.popleft()
            topo_order.append(course)
            
            # Decrease the indegree of the dependent courses
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Check if all courses are included in the topological order
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []