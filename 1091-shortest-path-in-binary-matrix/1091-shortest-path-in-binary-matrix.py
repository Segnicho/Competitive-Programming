class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1,0),(1,1),(-1,-1), (-1, 1), (1,-1), (-1,0),(0, -1)]
        m = len(grid)
        n = len(grid[0])
        def inbound(row, col):
            return 0 <= row < m and 0  <= col< n
        visited = set()
        def bfs(row, col):
            ans = 0
            if grid[row][col] == 0:
                q = deque([[row,col]])
            else:
                return -1
            while q:
                visited.add((0, 0))
                ans += 1
                size = len(q)
                for _ in range(size):
                    row, col = q.popleft()
                    for x, y in directions:
                        nwRow, nwCol = row + x, col + y
                        if inbound(nwRow, nwCol) and grid[nwRow][nwCol] == 0 and (nwRow, nwCol) not in visited:
                            q.append([nwRow, nwCol])
                            visited.add((nwRow, nwCol))
                        if nwRow == m and nwCol == n:
                            return ans
            return -1
        return bfs(0,0)
