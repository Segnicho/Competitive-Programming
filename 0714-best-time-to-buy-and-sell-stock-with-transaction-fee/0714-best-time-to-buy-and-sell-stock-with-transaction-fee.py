class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n= len(prices)
        @cache
        def dp(i=0, buy= True):
            if i >= n:
                return 0
            if buy:
                return max( -prices[i] + dp(i+1, False) , dp(i+1, True))
            else:
                return max( prices[i] - fee + dp(i+1, True) , dp(i+1, False))
        return dp()