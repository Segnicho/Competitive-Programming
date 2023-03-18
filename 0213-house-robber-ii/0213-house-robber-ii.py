class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def dp(i, n):
            if i >= n:
                return 0
            return max(nums[i] + dp(i+2, n), dp(i+1, n) )
        return max(dp(0, len(nums) -1), dp(1, len(nums)))
    