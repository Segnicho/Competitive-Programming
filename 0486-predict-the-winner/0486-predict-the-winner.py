class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(l,r,p1,p2,turn):
            if r < l:
                return p1 >= p2
            if turn:
                # player 1 gets to pick
                return dp(l + 1, r, p1 + nums[l] , p2, not turn) or dp(l, r - 1, p1 + nums[r] ,p2,not turn)
            
            else:
                return (dp(l + 1, r, p1 ,p2+ nums[l],not turn) and dp(l, r - 1, p1 ,p2 + nums[r] , not turn))
        
        return dp(0, len(nums)-1, 0, 0, True)