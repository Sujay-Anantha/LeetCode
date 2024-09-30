class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
# Initialize the closest number to a large positive number (or first element)
        closest = nums[0]
        
        # Iterate through the array
        for num in nums:
            # If this number is closer to zero, or it's the same distance but larger, update closest
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        
        return closest
