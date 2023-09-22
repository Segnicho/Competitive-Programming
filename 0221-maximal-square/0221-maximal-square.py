class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        res = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j]) +1
                    res = max(res, dp[i][j])
        return res*res
    
                    