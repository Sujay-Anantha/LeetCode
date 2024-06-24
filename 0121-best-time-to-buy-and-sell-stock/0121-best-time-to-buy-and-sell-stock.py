class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            max_profit = max(prices[i]-buy,max_profit)
            buy = min(buy,prices[i])
        
        return max_profit
        
 
            
'''
7,5,3,6,1,4
      i

7,5,3,6,1,4
        j

'''