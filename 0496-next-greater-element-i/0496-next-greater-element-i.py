class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         greater_list = []
#         n = len(nums2)
#         for num in nums1:
#             idx = nums2.index(num)
#             #print(idx)
#             if idx == n:
#                 greater_list.append(-1)
#             else:
#                 for i in range(idx, n):
#                     if nums2[i] > num:
#                         print(nums2[i])
#                         greater_list.append(nums2[i])
#                         break
                
#                 greater_list.append(-1)
        
        
#         return greater_list
        greater_list = []
        n = len(nums2)
        
        for num in nums1:
            idx = nums2.index(num)
            found = False  # Flag to track if a greater element is found
            for i in range(idx + 1, n):  # Start from idx + 1, not idx itself
                if nums2[i] > num:
                    greater_list.append(nums2[i])
                    found = True
                    break
            
            if not found:
                greater_list.append(-1)
        
        return greater_list