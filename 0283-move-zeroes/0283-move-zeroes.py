class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # for i in range(0,len(nums)-1):
        #     if nums[i] == 0:
        #         nums.insert(len(nums) - 1, nums.pop(i))
                
        lastNonZeroFoundAt = 0
    
        for current in range(len(nums)):
            # print(nums)
            if nums[current] != 0:
                nums[lastNonZeroFoundAt], nums[current] = nums[current], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1
                #print(nums)