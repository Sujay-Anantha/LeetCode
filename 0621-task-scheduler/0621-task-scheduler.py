class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        # Count the frequency of each task
        task_counts = Counter(tasks)
        # Create a max heap based on the task counts
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        # Queue to keep track of the cooldown period for tasks
        cooldown_queue = deque()
        
        while max_heap or cooldown_queue:
            time += 1
            
            if max_heap:
                count = 1 + heapq.heappop(max_heap)  # Pop the most frequent task
                if count:  # If there are more instances of this task, put it in the cooldown queue
                    cooldown_queue.append((count, time + n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
        
        return time