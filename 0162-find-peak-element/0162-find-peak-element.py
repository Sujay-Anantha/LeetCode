class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # Check the mid element with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # There must be a peak in the left half (including mid)
                r = mid
            else:
                # There must be a peak in the right half
                l = mid + 1
        
        # l and r will converge to the peak index
        return l
