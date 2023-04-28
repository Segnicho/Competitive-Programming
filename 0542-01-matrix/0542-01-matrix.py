class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1,0), (-1,0),(0, -1)]
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = set()
        res = []
        
        def inbound(row, col):
            return 0 <= row < m and 0  <= col< n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
                else:
                    grid[i][j] = -1
        while q:
            r, c = q.popleft()
            for x, y in directions:
                row = r + x
                col = y + c
                if inbound(row, col) and (row, col) not in visited:
                    grid[row][col] = grid[r][c] + 1
                    q.append((row, col))
                    visited.add((row, col))
        return grid
    
    