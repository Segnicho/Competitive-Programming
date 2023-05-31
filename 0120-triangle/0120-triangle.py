class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        @cache
        def dp(i, j):
            if i >= m:
                return 0
            if j >= len(triangle[i]):
                return float("inf")
            
            return triangle[i][j] + min(dp(i+1, j), dp(i+1, j+1))            
        return dp(0, 0)