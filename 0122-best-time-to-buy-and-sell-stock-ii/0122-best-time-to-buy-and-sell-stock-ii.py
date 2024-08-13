class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = None
        profit = 0
        n = len(prices) 
        for i in range(1,n):
            
            if prices[i-1] < prices[i] and buy is None:
                buy = prices[i-1]
                print(buy)
            if prices[i-1] > prices[i] and buy is not None:
                profit += prices[i-1] - buy
                print(profit)
                buy = None
        if buy is not None:
            profit += prices[n-1] - buy
                
        return profit
                
            