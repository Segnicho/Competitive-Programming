class Solution:
    def fib(self, n: int) -> int:
#         def dp(i):
#             if i == 0 or i == 1:
#                 return i
#             return dp(i-2)+ dp(i-1)
#         return dp(n)
        
        dp = [0] * (n + 1)
        for i in range(len(dp)):
            if i == 0 or i == 1:
                dp[i] =  i
                continue
            dp[i] =  dp[i-2]+ dp[i-1]
        return dp[n]