class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currProfit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                currProfit = prices[i] - prices[i-1]
                profit+=currProfit
        return profit 
        
        