class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        memo = defaultdict()
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n or j == n:
                return 0
            if s[i] == t[j]:
                return 1 + dp(i+1, j+1)
            memo[(i, j)] = max(dp(i, j+1), dp(i+1, j))
            
            return memo[(i, j)]
        return dp(0, 0)