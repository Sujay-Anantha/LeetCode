class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing_ranges = []
        if not nums:
            return [[lower,upper]]
        for num in nums:
            if lower in nums:
                lower += 1
            else:
                missing_ranges.append([lower,num-1])
                lower = num + 1
        if nums[len(nums)-1]!=upper:
            missing_ranges.append([lower,upper])
        
        return missing_ranges
            
        
        