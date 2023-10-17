class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @cache
        def dp(i, isEven):
            if i >= len(nums):
                return 0
            
            notTake = dp(i+1, isEven)
            take = -math.inf
            if isEven:
                take = nums[i] + dp(i + 1, False)
            else:
                take = dp(i+1, True) - nums[i]
            return max(take, notTake)
        
        return max(dp(0, True), dp(0, False) )