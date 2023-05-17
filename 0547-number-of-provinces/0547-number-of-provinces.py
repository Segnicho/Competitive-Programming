class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.getComponents()
        
        
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.components = 0
    
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
    def getComponents(self):
        for  i,num in enumerate(self.root):
            if i == num:
                self.components += 1
        return self.components
