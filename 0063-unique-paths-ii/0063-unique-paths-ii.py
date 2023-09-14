class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        @cache
        def dp(i, j):
            if i <0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0: return 1
            up = dp(i-1, j)
            left = dp(i, j-1)
            
            return left + up
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0]) 
        return dp(n-1, m-1)