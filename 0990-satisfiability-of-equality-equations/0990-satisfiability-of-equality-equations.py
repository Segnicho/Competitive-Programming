class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFind(26)
        for string in equations:
            if string[1] == "=":
                firstCh = string[0]
                lastCh = string[-1]
                uf.union(ord(firstCh)-ord("a"), ord(lastCh)-ord("a"))
        for string in equations:
            if string[1] == "!":
                firstCh = string[0]
                lastCh = string[-1]
                if uf.find(ord(firstCh)-ord("a")) == uf.find(ord(lastCh)-ord("a")):
                    return False
        return True
         
        
        
        
        
        
        
        
        
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
        
        