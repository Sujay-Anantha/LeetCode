class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        buy,sell = prices[0],0
        n = len(prices)        
        for j in range(1,n):
            buy = min(buy,prices[j])
            sell = max(sell, prices[j]-buy)
        
        return sell
            
                
