class Solution:
    def fib(self, n: int) -> int:
#         def dp(i):
#             if i == 0 or i == 1:
#                 return i
#             return dp(i-2)+ dp(i-1)
#         return dp(n)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,len(dp)):
            dp[i] =  dp[i-2]+ dp[i-1]
        return dp[n]