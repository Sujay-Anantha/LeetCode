class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        ans = float('inf')
        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans,nums[l])
            else:
                ans = min(ans, nums[r])
            
            l += 1
            r -= 1
        
        return ans
            
        