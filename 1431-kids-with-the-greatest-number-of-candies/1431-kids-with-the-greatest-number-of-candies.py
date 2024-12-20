class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        greatest = max(candies)
        for candy in candies:
            if candy + extraCandies >= greatest:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
        