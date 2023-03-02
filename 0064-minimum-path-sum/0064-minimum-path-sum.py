class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i,j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[-1][-1]
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return grid[i][j] + min(dp(i+ 1,j),  dp(i, j + 1))
            else:
                return float("inf")
        return dp(0,0)