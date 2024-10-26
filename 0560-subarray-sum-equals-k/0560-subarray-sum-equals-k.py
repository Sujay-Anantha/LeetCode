class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_count = defaultdict(int)
        cumulative_sum_count[0] = 1  # This accounts for subarrays starting from index 0
        
        current_sum = 0
        answer = 0
        
        for num in nums:
            current_sum += num
            
            # Check if there is a subarray sum that equals k
            if (current_sum - k) in cumulative_sum_count:
                answer += cumulative_sum_count[current_sum - k]
            
            # Update the count of the current_sum in the dictionary
            cumulative_sum_count[current_sum] += 1
        
        return answer