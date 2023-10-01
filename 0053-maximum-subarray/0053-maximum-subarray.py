class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        @cache
        def dp(i, pick):
            if i >= n:
                return 0 if pick else -math.inf
            if pick:
                return max(0, nums[i]+ dp(i+1, True))
            return max(dp(i+1, False), nums[i]+ dp(i+1, True))

        return dp(0, False)