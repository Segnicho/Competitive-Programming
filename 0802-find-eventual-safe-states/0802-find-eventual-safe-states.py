class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        res = []
        outDegree = defaultdict()
        q = deque()
        
        for i, num in enumerate(graph):
            for n in num:
                g[n].add(i)
            outDegree[i] = len(num)
            if not num:
                q.append(i)
        while q:
            curr = q.popleft()
            res.append(curr)
            for parent in g[curr]:
                if outDegree[parent] == 1:
                    q.append(parent)
                outDegree[parent] -= 1
        res.sort()
        return res