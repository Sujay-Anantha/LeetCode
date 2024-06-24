class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # If either nums1 or nums2 is empty, there are no pairs to form
        if not nums1 or not nums2:
            return []

        # Min-heap to store the pairs along with their sums
        min_heap = []
        result = []
        
        # Initialize the heap with the first element from nums1 and every element from nums2
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # Extract the smallest pairs from the heap until we have k pairs
        while min_heap and len(result) < k:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If there are more elements in nums2 to pair with nums1[i], add them to the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result
        