class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)
        for i in range(len(s1)):
            uf.union(ord(s1[i])-ord("a"), ord(s2[i])-ord("a"))
        res = []
        for ch in baseStr:
            for i in range(26):
                if uf.find(i) == uf.find(ord(ch)-ord("a")):
                    res.append(chr(i+ord("a")))     
                    break
        return "".join(res)
        
        

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
        