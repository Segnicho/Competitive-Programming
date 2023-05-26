class Solution:
    def climbStairs(self, n: int) -> int:
        # @cache
        dikt = defaultdict(int)
        def dp(i):
            if i == 1:
                return 1
            elif  i == 2:
                return 2
            if dikt[i]:
                return dikt[i]
            res = dp(i-2) + dp(i-1)
            dikt[i] = res 
            return res
        return dp(n)
    
    