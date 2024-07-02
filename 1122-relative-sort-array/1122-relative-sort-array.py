class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
         # Create a dictionary to map the elements of arr2 to their indices
        order_map = {value: index for index, value in enumerate(arr2)}
        
        # Separate arr1 into two parts: in arr2 and not in arr2
        in_arr2 = [x for x in arr1 if x in order_map]
        not_in_arr2 = [x for x in arr1 if x not in order_map]
        
        # Sort in_arr2 based on the order defined by arr2
        in_arr2.sort(key=lambda x: order_map[x])
        
        # Sort not_in_arr2 in ascending order
        not_in_arr2.sort()
        
        # Combine the sorted parts
        return in_arr2 + not_in_arr2
            