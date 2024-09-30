class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize the answer array with 1
        
        # Step 1: Compute the left product for each element
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]  # Update left_product to include nums[i]
        
        # Step 2: Compute the right product and multiply it with the left product
        right_product = 1
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            answer[i] *= right_product
            right_product *= nums[i]  # Update right_product to include nums[i]
        
        return answer
        