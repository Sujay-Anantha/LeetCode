class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        sqrt = {}
        max_num = 1
        for y in range(x):
            sqrt[y] = y*y
            if sqrt[y] > x:
                break
            max_num = max(max_num,y)
        
        return max_num
        