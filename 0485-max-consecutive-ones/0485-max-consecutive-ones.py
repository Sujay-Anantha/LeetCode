class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_check, max_check = 0,0
        for num in nums:
            if num == 1:
                current_check += 1
            else:
                current_check = 0
            
            max_check = max(max_check, current_check)
        
        return max_check