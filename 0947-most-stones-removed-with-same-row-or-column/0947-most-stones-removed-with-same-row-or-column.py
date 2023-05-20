class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(n)
        dik = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        res = defaultdict(int)
        for i in range(n):
            root = uf.find(i)
            res[root] += 1     
        ans = 0
        for num in res.values():
            ans += (num-1)
        return ans

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
        
        
        