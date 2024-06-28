class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = Counter(nums)
        for keys in numbers.keys():
            if numbers[keys]>= 2:
                return True
        # if numbers > 2:
        #     return False
        return False
        