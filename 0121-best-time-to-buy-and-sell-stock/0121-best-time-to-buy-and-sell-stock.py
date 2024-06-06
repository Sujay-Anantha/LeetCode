class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            
            # Calculate potential profit with the current price and update max profit
            potential_profit = price - min_price
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit
            
            
            
'''
7,5,3,6,1,4
      i

7,5,3,6,1,4
        j

'''