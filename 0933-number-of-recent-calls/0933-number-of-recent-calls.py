class RecentCounter:

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        # Upon Ping add new ping to queue
        self.queue.append(t)

        # Remove all ping in queue with value more than 3000 away from new ping
        while self.queue and self.queue[0] + 3000 < t:
            self.queue.popleft()
        
        # Return length of queue
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)