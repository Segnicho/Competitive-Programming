class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 1
            res = 0
            for j in range(1, i+1):
                res += dp(j-1) * dp(i-j)
            return res
        return dp(n)