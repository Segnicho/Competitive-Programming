class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ans = defaultdict(set)
        for start, end in edges:
            graph[start].append(end)
        
        indegree = Counter()
        q = deque()
        seen = set()
        for ky, val in graph.items():
            ky not in seen and q.append(ky) 
            for num in val:
                seen.add(num)
                indegree[num] += 1
                if num in q:
                    q.remove(num)
        while q:
            curr = q.popleft()
            for num in graph[curr]:
                {ans[num].add(val) for val in ans[curr]}
                ans[num].add(curr)
                if indegree[num] == 1:
                    q.append(num)
                indegree[num] -= 1
        res = []
        for i in range(n):
            if i not in ans:
                res.append([])
            else:
                val = list(ans[i])
                val.sort()
                res.append(val)
        return res
                    