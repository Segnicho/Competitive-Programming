class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        res = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(row, col):
            if not visited[row][col] and grid[row][col] == 1:
                if  grid1[row][col] == 0:
                    self.t = False
                visited[row][col] = True
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if inbound(new_row, new_col):
                        dfs(new_row, new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    self.t = True
                    dfs(i, j)
                    if self.t:
                        res += 1 
        return res