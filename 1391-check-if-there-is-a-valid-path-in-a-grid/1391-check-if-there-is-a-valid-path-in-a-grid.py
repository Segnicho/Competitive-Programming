class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        uf  = UnionFind(m*n)
        dikt = defaultdict(list)
        
        dikt[1] = set([1, 5, 3])
        dikt[4] = set([1,3, 5])
        dikt[6] = set([5, 3, 1])
        
        coldikt = defaultdict(set)
        
        coldikt[2] = set([2, 5, 6])
        coldikt[3] = set([5, 6, 2])
        coldikt[4] = set([5, 6, 2])
        
        for i in range(m):
            for j in range(n):
                if j-1 >= 0 and grid[i][j] in dikt[grid[i][j-1]]:
                    uf.union(n*i + j, n*i+j-1) 
                if i-1 >= 0 and grid[i][j] in coldikt[grid[i-1][j]]:
                    uf.union(n*i + j, n*(i - 1)+j)      
        return uf.isConnected(0, m * n -1)    
    
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.ans = []
    def find(self, u):
        if self.root[u] == u:
            return u
        self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        if rootu == rootv:
            self.ans = [u+1, v+1]
        if rootu != rootv:
            if self.rank[rootu] > self.rank[rootv]:
                self.root[rootv] = rootu
            elif self.rank[rootv] > self.rank[rootu]:
                self.root[rootu] = rootv
            else:
                self.root[rootu] = rootv
                self.rank[rootv] += 1
    def isConnected(self, u, v):
        return self.find(u) == self.find(v)