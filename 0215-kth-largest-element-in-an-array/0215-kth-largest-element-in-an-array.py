class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap to store the k largest elements
        min_heap = []
        
        # Iterate over each number in the array
        for num in nums:
            heapq.heappush(min_heap, num)  # Push the current number to the heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove the smallest element if the heap grows beyond size k
        
        # The root of the heap will be the kth largest element
        return min_heap[0]