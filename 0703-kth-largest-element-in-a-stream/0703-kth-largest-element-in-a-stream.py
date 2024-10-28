import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Initialize the heap with the largest k elements from nums
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add the new value to the heap if we have fewer than k elements
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # Otherwise, if the new value is larger than the smallest in the heap, replace it
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        
        # The root of the heap is the k-th largest element
        return self.min_heap[0]
