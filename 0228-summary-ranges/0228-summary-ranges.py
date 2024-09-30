class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
#         answer = []
#         start = nums[0]
#         for i in range(1,len(nums)):
#             if start == nums[i] + 1:
                
#         result = []
#         n = len(nums)
        
#         if n == 0:
#             return result
        
#         start = nums[0]  # Start of the current range
        
#         for i in range(1, n):
#             # If nums[i] is not consecutive, finalize the previous range
#             if nums[i] != nums[i - 1] + 1:
#                 if start == nums[i - 1]:
#                     result.append(str(start))  # Single number
#                 else:
#                     result.append(f"{start}->{nums[i - 1]}")  # Range from start to previous element
#                 start = nums[i]  # Start new range
        
#         # Add the final range after the loop
#         if start == nums[-1]:
#             result.append(str(start))
#         else:
#             result.append(f"{start}->{nums[-1]}")
        
#         return result

        ans = []     
        i = 0 
        
        while i < len(nums): 
            start = nums[i]  
            while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            if start != nums[i]: 
                ans.append(str(start) + "->" + str(nums[i]))
            else: 
                ans.append(str(nums[i]))
            
            i += 1

        return ans