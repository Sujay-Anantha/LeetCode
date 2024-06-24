class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store:
                return [i,store[diff]]
            store[nums[i]] = i 
            
                
