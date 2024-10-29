class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)  # Count occurrences in nums1
        result = []
        
        for num in nums2:
            if counts[num] > 0:  # If num is in nums1 and count is non-zero
                result.append(num)
                counts[num] -= 1  # Decrement count to handle duplicates properly
        
        return result
        
        