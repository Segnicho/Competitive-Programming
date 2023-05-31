class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(n)] for i in range(m)]
        res[0] = [1]*n
        for i in range(m):
            res[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] =  res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]