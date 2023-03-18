class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i, n):
            if i >= n:
                return 0
            return max(nums[i] + dp(i+2, n), dp(i+1, n) )
        return max(nums[0], dp(0, len(nums) -1), dp(1, len(nums)))
    