class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i,canBuy,count):
            if i == len(prices) or count == 0:
                return 0
            # can buy
            if canBuy:
                return max(dp(i + 1, False,count - 1) - prices[i],dp(i + 1, True,count))
            else:
                return max(prices[i] + dp(i + 1, True,count - 1),dp(i + 1, False, count))
        return dp(0,True, 2 * 2)
            
            