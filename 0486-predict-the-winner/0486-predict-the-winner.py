class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
                                    
        @cache
        def dp(l,r):
            if r == l:
                return nums[l]
            else:
                return max(nums[l] - dp(l+1, r), nums[r] - dp(l, r-1))
        return dp(0, len(nums)-1) >= 0