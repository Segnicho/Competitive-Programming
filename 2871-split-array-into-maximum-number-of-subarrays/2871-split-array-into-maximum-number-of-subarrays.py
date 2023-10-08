class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        
        res= -1
        ans = 0
        for num in nums:
            res = num & res
            if res == 0:
                ans += 1
                res = -1
        
        return max(ans, 1)