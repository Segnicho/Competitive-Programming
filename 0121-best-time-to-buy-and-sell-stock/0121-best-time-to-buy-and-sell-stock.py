class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float("inf")
        res = 0
        for i in range(len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            else:
                res = max(res, prices[i] - mn)
        
        return res