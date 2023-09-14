class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mp = defaultdict(int)
        def dp(i, j):
            if mp[(i, j)]:
                return mp[(i,j)]
            if i == m-1 and j == n-1:
                return 1
            if i >=m or j >=n:
                return 0
            down  = dp(i+1, j)
            right  = dp(i, j+1)
            res = down + right
            mp[(i, j)]  =res
            return res
               
        return dp(0, 0)