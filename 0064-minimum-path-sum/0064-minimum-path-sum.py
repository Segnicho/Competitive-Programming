class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def dp(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            elif i <0 or j < 0:
                return float("inf")
            up = grid[i][j] + dp(i-1, j)
            left = grid[i][j] + dp(i, j-1)            
            return min(up, left)
        return dp(m-1, n-1)