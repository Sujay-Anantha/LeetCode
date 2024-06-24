class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]
        indexes = {}
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                sum_value = nums[i] + nums[j]
                indexes[sum_value] = [i,j]
        return indexes[target]
            
                
