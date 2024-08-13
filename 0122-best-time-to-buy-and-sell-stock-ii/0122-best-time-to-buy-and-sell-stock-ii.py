class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                  maxProfit += (prices[i] - prices[i - 1])

        return maxProfit
            