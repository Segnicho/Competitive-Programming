class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def dfs(grid, visited, row, col):
            if not inbound(row, col) or grid[row][col] == "0" or visited[row][col]:
                return
            
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                dfs(grid, visited, new_row, new_col)
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not visited[row][col]:
                    res += 1
                    dfs(grid, visited, row, col)
        return res