class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target  = sum(nums)/2
        if sum(nums) %2 == 1: 
            return False
        
        
        def dp(i, curr):
                        
            if memo[i][curr] != -1:
                return memo[i][curr]

            if curr == target: 
                return True

            if i >= n or curr > target:
                return False
            take = dp(i+1, curr+nums[i])
            notTake = dp(i+1, curr)
            memo[i][curr] = take or notTake
            
            return memo[i][curr] 


        n = len(nums)
        memo = [[-1 for i in range(10100)] for j in range(n+10)]
        
        return dp(0, 0)
            
            