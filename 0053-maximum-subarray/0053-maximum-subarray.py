class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]]*n
        
        for i in range(1, n):
            dp[i] = max(dp[i-1]+ nums[i] , nums[i])
        
        return max(dp)