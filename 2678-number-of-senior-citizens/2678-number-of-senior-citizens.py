class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passengers in details:
            if passengers[11:13] > '60':
                count += 1
        
        return count
        