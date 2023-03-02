class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i,allowed):
            if i == len(nums) - 1:
                return nums[i] if allowed else 0
            if allowed:
                return max(nums[i] + dp(i + 1,False),dp(i + 1, True))
            else:
                return dp(i + 1,True)
        return dp(0,True)