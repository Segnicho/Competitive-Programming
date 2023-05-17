class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.isConnected(source, destination)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
    
    def find(self, u):
        if self.root[u] == u:
            return u
        self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        rootu = self.find(u)
        rootv = self.find(v)
        if self.rank[rootu] > self.rank[rootv]:
            self.root[rootv] = rootu
        elif self.rank[rootv] > self.rank[rootu]:
            self.root[rootu] = rootv
        else:
            self.root[rootu] = rootv
            self.rank[rootv] += 1
    def isConnected(self, u, v):
        return self.find(u) == self.find(v)
