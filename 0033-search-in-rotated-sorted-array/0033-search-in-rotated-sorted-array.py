class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # If the target is found, return the index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # Check if the target is within the left half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # The right half must be sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        # Target is not found
        return -1
