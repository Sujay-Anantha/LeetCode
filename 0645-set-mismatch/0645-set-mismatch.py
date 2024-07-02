class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = sum(nums)
        nums1 = set(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum1 = sum(nums1)
        return [actual_sum - actual_sum1, expected_sum - actual_sum1]
        