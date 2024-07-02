class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        if len(nums1)>=len(nums2):
            for num in nums2:
                if num in nums1 and num not in common:
                    common.append(num)
        else:
            for num in nums1:
                if num in nums2 and num not in common:
                    common.append(num)
            
        return common