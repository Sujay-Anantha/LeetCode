class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         n = len(intervals)
#         answer = []
#         l = 0
#         i = float('inf')
#         j = float('-inf')
#         while l<n-1:
#             if intervals[l][0] <= intervals[l+1][0] <= intervals[l][1]:
#                 i = min(intervals[l][0],i)
#                 j = max(intervals[l+1][1],j)
#                 l += 1
#             else:
#                 i = intervals[l][0]
#                 j = intervals[l][1]
#             answer.append([i,j])
#             l += 1
        
#         return answer
        if not intervals:
            return []
        
        # Step 1: Sort intervals by the starting time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize the merged intervals list with the first interval
        merged = [intervals[0]]
        
        # Step 3: Traverse the intervals and merge where necessary
        for i in range(1, len(intervals)):
            # Get the last interval in the merged list
            last_interval = merged[-1]
            
            # If the current interval overlaps with the last merged interval, merge them
            if intervals[i][0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], intervals[i][1])
            else:
                # Otherwise, just add the current interval to the merged list
                merged.append(intervals[i])
        
        return merged
            
        