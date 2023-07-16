class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < n
        @cache
        def dp(i, j):
            if i >= n :
                return 0
            if not inbound(i, j):
                return float("inf")
            if inbound(i, j):
                return min(matrix[i][j]+ dp(i+1, j), \
                          matrix[i][j]+ dp(i+1, j+1), \
                           matrix[i][j]+ dp(i+1, j-1)
                          )
        mn = float("inf")
        for r in range(n):
            mn = min(mn, dp(0, r))
        return mn