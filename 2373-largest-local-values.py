class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        def getMax(grid, ix, jx):
            mx = 0
            for ix in range(ix, ix+3):
                for j in range(jx, jx+3):
                    # print(ix,j)
                    temp  = grid[ix][j]
                    mx = max(temp,mx)
            return mx
        for i in range(n-2): 
            for j in range(n-2):
                ans[i][j] = getMax(grid, i, j)
        return ans
