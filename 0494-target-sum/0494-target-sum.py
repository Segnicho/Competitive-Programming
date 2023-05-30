class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = defaultdict(int)
        @lru_cache(maxsize = None)
        def dp(i, targetSum):
            if i >= n:
                if targetSum == target:
                    return 1
                return 0            
    
            return dp(i+ 1,  targetSum + nums[i]) + dp(i + 1 , targetSum - nums[i]) 

        return dp(0, 0)
    