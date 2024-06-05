class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if (x<0) or (x%10  == 0 and x != 0):
            return False
        
        j = 0
        while x > j:
            
            j = j * 10 + (x % 10)
            x = x // 10
        
        return x == j or x == j//10

        
        
        
#         Umpire:
#             Understand:
                            # what if the x is length 1?
                            # what if the x is 0?
            
#             Match/Map:
            
#             Plan:
                
#             Implement:
                
#             Review:

'''
121

x = 121
j = 0

j = 1
x =12

j =12
x =1 

return x = 1 and j 1
'''

#             Evaluate:
            