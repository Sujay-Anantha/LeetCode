class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each element
        freq = Counter(nums)
        
        # Step 2: Sort by frequency (ascending), then by value (descending)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        
        return sorted_nums