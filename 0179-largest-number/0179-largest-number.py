class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #
        '''
        3,30,34,5,9
        i, j
        3,30,34,5,9
           i, j
        3,34,30,5,9
              i,j  
        3,34,5,30,9
                i,j
        3,34,5,9,30    
        '''
# Custom comparator to sort based on string concatenation
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # they are equal
        
        # Convert all numbers to strings for comparison
        nums = list(map(str, nums))
        
        # Sort using the custom comparator
        nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers
        result = ''.join(nums)
        
        # Edge case: if the result starts with '0', return '0'
        return '0' if result[0] == '0' else result