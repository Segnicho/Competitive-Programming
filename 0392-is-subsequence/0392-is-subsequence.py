class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        # @cache
        def dp(i, j):
            if i >= m:
                return True
            if j >= n and i < m:
                return False
            if s[i]== t[j]:
                return dp(i+1, j+1)
            else:
                return dp(i, j+1)
        return dp(0, 0)