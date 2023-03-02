class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            if i == len(nums) - 1:
                return 0
            res = float("inf")
            for j in range(i + 1, min(len(nums),i + nums[i] + 1)):
                res = min(res, 1 + dp(j))
            return res
        return dp(0)