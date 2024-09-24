class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Create a max heap (negative frequency for max-heap behavior in Python)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        # Step 3: Rebuild the string
        result = []
        prev_count, prev_char = 0, ""
        
        while max_heap:
            # Pop the most frequent character
            count, char = heapq.heappop(max_heap)
            result.append(char)
            
            # If the previous character still has remaining count, push it back into the heap
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            
            # Update prev_count and prev_char to the current one, with one less count
            prev_count, prev_char = count + 1, char  # Decrease the count (closer to 0)
        
        # Step 4: Join the result list into a string
        reorganized_string = "".join(result)
        
        # Check if the resulting string is valid (length should be same as original)
        if len(reorganized_string) != len(s):
            return ""
        
        return reorganized_string

        
        