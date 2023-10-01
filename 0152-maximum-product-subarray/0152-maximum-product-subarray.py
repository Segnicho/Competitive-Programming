class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(i, num):
            if i >= n:
                return num
            
            op1 = dp(i+1,num *nums[i])
            op2 = dp(i+1, nums[i])
            return max(op1, op2, num)
        return dp(1, nums[0])