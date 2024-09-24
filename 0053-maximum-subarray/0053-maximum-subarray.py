class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# Initialize current_sum and max_sum with the first element of the array
        current_sum = max_sum = nums[0]
        
        # Iterate through the rest of the array, starting from the second element
        for num in nums[1:]:
            # Either add the current number to the current sum or start a new subarray from the current number
            current_sum = max(num, current_sum + num)
            
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum