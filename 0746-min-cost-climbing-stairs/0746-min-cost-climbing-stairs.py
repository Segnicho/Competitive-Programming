class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def dp(i):
            if i >= n:
                return 0
            return cost[i] + min(dp(i+2) , dp(i+1))
        return min(dp(0), dp(1))
    