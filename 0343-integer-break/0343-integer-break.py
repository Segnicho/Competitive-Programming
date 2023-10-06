class Solution:
    def integerBreak(self, n: int) -> int:
        if n< 4: return n-1
        @cache
        def dp(prod):
            if prod < 4:
                return prod
            num = prod
            for i in range(2, prod):
                num = max(num, i * dp(prod-i))
            return num
        
        return dp(n)