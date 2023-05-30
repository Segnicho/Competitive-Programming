class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        n = len(nums)
        memo = defaultdict(int)
        def dp(i, targetSum):
            if i >= n:
                if targetSum == target:
                    return 1
                return 0            
            state = (targetSum, i)
            if state not in memo:
                memo[state] = dp(i+ 1,  targetSum + nums[i]) + dp(i + 1 , targetSum - nums[i]) 
            return memo[state]
        return dp(0, 0)
    