class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize pointers
        i = m + n - 1  # Pointer for the last position in nums1
        p1 = m - 1     # Pointer for the last element in the initial part of nums1
        p2 = n - 1     # Pointer for the last element in nums2

        # Merge nums2 into nums1 starting from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1

        # If there are elements left in nums2, copy them
        while p2 >= 0:
            nums1[i] = nums2[p2]
            i -= 1
            p2 -= 1