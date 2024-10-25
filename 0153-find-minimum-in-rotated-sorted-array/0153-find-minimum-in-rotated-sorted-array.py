class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            # If the middle element is greater than the rightmost element,
            # then the minimum must be in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is in the left half (including mid)
            else:
                r = mid
                
        return nums[l]
