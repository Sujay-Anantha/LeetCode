class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maximum = max(nums)
        
        # if len(nums) >2:
        #     maximum = max(nums[1:len(nums)-1])
        
        
        
        return nums.index(maximum)
        
            
        