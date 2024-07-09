class RecentCounter:

    def __init__(self):
        self._start = 0
        self._range = []
        

    def ping(self, t: int) -> int:
        # add request to requests
        self._range.append(t)

        # get the range
        cur_start, cur_end = t-3000, t

        # check if start is not within range
        while self._range[self._start] < cur_start:
            
            # incr the start
            self._start += 1

        return len(self._range) - self._start
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)