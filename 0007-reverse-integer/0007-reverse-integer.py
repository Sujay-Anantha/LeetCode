class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x = abs(x)
        
        mer = 0
        while x > 0:

            m = x % 10
            mer = (mer * 10) + m 
            x  = x // 10
        
        if -2**31 > mer or mer > (2**31)-1:
            return 0
        
        mer = mer * neg
            
        return mer
        
        