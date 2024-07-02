class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        while True:
            if num not in nums:
                return num
            num += 1
            
        