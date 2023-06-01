class Solution:
    def longestPalindromeSubseq(self, text1: str) -> int:
        text2 = text1[::-1]
        m = len(text1)
        n = len(text2)        
        @cache
        def dp(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)
            return max(dp(i+1, j), dp(i, j+1))
        return dp(0, 0)
        