class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        @cache
        def dp(i, left, right):
            if i >= m: return 0
            num = multipliers[i]
            chooseLeft = dp(i+1, left+1, right)
            chooseRight = dp(i+1, left, right-1)
            return max(num*nums[left] + chooseLeft, num*nums[right]+chooseRight)
        
        return dp(0, 0, n-1)
        