class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailMap = defaultdict(int)
        for i, email in enumerate(accounts):
            for e in email[1:]:
                if e in emailMap:
                    uf.union(i, emailMap[e])
                else:
                    emailMap[e] = i
        group = defaultdict(list)
        for email, idx in emailMap.items():
            head = uf.find(idx)
            group[head].append(email)
        res = []
        for idx, emails in group.items():
            name = accounts[idx][0]
            res.append([name]+ sorted(emails))
        return res
        
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
        