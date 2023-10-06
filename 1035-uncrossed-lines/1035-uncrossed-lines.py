class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if nums1[i] == nums2[j]:
                memo[(i, j)] =  1 + dp(i+1, j+1)
            else:
                memo[(i, j)] = max(dp(i, j+1), dp(i+1, j))
            return memo[(i, j)]
        
        memo = {}
        return dp(0, 0)
    