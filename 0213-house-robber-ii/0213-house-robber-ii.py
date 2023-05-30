class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(maxsize = None)
        def dp(i, size):
            if i >=size:
                return 0
            return max(nums[i]+dp(i+2, size), dp(i+1, size))
        return max(nums[0], dp(0, n-1), dp(1, n)) 
