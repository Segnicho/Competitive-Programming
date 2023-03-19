class Solution:
    def numTrees(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]
        
        @cache
        def findFact(num):
            if num <= 1:
                return 1
            return num*findFact(num-1)
        return findFact(2*n)//(findFact(n+1) * findFact(n))