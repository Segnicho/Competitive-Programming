class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= m or j >= n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            memo[(i, j)] = max( dp(i, j+1),  dp(i+1, j))
            return memo[(i, j)]
        
        m = len(text1)
        n= len(text2)
        memo = {}
        return dp(0, 0)
    