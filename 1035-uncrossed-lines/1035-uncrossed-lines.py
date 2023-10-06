class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        @cache
        def dp(i, j):
            if i >= m or j >= n:
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dp(i+1, j+1)
            else:
                return max(dp(i, j+1), dp(i+1, j))
        
        return dp(0, 0)