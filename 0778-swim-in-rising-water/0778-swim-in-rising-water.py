class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        def inbound(x, y):
            return 0<=x<n and 0<=y<n
        q = [[grid[0][0], (0, 0)]]
        distances = defaultdict()
        for i in range(n):
            for j in range(n):
                distances[(i, j)] = -math.inf
                
        distances[(0, 0)] = grid[0][0]
        directions = [(1, 0), (0, 1),(0, -1), (-1, 0)]
        visited = set()
        while q:
            dist, cell = heappop(q)
            if cell in visited:
                continue
            visited.add(cell)
            if cell == (n-1, n-1):
                return dist
            for i, j in directions:
                x, y = cell[0]+i, cell[1]+j
                if inbound(x, y):
                    distance = max(dist, grid[x][y])
                    distances[(x, y)] = distance
                    heappush(q, [distance, (x, y)])
                    
        