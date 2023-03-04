class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def hr(idx):
            if idx >= len(nums):
                return 0
            return max(nums[idx] + hr(idx+2), hr(idx+1))
        return hr(0)
    