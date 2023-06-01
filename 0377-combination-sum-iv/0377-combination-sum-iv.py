class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(sm):
            if sm > target:
                return 0
            if sm == target:
                return 1
            res = 0
            for num in nums:
                res += dp(sm+num)
            return res
        return dp(0)