class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater_map = {}
        stack = []
        
        # Traverse nums2 and populate next_greater_map
        for num in nums2:
            # While stack is not empty and the current num is greater than the stack's top
            while stack and num > stack[-1]:
                smaller_num = stack.pop()  # Pop the smaller number from the stack
                next_greater_map[smaller_num] = num  # Map it to the current number as its next greater element
            stack.append(num)  # Push the current number onto the stack
        
        # Elements left in the stack have no next greater element, map them to -1
        while stack:
            smaller_num = stack.pop()
            next_greater_map[smaller_num] = -1
        
        # For each num in nums1, find the next greater element from the map
        return [next_greater_map[num] for num in nums1]

#         greater_list = []
#         n = len(nums2)
        
#         for num in nums1:
#             idx = nums2.index(num)
#             found = False  # Flag to track if a greater element is found
#             for i in range(idx + 1, n):  # Start from idx + 1, not idx itself
#                 if nums2[i] > num:
#                     greater_list.append(nums2[i])
#                     found = True
#                     break
            
#             if not found:
#                 greater_list.append(-1)
        
#         return greater_list
