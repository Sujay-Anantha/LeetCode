class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# Dictionary to store value -> index pairs
        num_to_index = {}
        
        # Loop through each number in the list
        for i, num in enumerate(nums):
            # Calculate the complement (what we need to find)
            complement = target - num
            
            # If the complement is already in the dictionary, return the indices
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = i
