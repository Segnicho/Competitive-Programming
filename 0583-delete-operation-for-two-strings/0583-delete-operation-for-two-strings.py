class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @lru_cache(None)
        def dp(i=0, j=0):
            if i == n  and j == m:
                return 0
            elif i == n:
                return m-j
            elif j == m:
                return n-i
            elif word1[i] == word2[j]:
                 return dp(i+1,j+1)
            else: 
                return min(dp(i+1, j),dp(i, j+ 1)) + 1
            
        return dp()