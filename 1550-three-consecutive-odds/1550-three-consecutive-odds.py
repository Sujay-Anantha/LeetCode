class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for num in arr:
            
            if num % 2 == 1:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
            
        return False
        