class Solution:
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        nums = []
        
        for i in range(1, int(n**0.5) + 1):
            nums.append(i)
        
        dp[0] = 0
        
        for i in range(1, n + 1):
            for num in nums:
                sqr = num*num
                if sqr <= i:
                    dp[i] = min(dp[i - (sqr)] + 1, dp[i])
                else:
                    break
        return dp[n]
