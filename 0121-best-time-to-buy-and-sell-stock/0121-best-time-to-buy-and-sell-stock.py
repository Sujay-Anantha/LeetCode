class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        sell = 0
        #print(len(prices)-1)
        for i in range(1, len(prices)):
            moving = prices[i]
            #print(moving)
            
            
            buy = min(moving, buy)
            # if buy < moving
            #     sell = buy - min()
                
            #print(f'Buy = ', buy)    
            
            sell = max(sell, moving -buy)
            
            #print(f'Sell = ',sell)
            
        return sell
            
            
            
'''
7,5,3,6,1,4
      i

7,5,3,6,1,4
        j

'''