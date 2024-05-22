class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        ind = 2  # Start from the third position
        
        for i in range(2, len(nums)):
            if nums[i] != nums[ind - 2]:
                nums[ind] = nums[i]
                ind += 1
        
        return ind