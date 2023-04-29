class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        m = len(maze)
        n = len(maze[0])
        def bfs(row, col):
            q = deque([[row, col]])
            visited.add((row, col))
            ans = 0
            while q:
                ans += 1
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for x, y in directions:
                        nrow = x + row
                        ncol = y + col
                        if 0 <= nrow < m and 0 <= ncol < n and maze[nrow][ncol] == "." and (nrow, ncol) not in visited:
                            if (nrow == 0 or ncol == 0 or nrow == m- 1 or ncol == n-1):
                                return ans
                            q.append([nrow, ncol])
                            visited.add((nrow, ncol))
                        
            return -1
        
        return bfs(entrance[0], entrance[1])
        