class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dp(i, j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            if i >= m or j >= n:
                return float("inf")
            return min(grid[i][j] + dp(i+1, j), grid[i][j]+dp(i, j+1))
        return dp(0, 0)