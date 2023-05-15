class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        if n == 1:
            return [0]
        for start, end in edges:
            graph[start].append(end)    
            graph[end].append(start)
            indegree[start] += 1
            indegree[end] += 1
            
        q = deque()
        for ky, val in graph.items():
            if len(val) == 1:
                q.append(ky)
        cnt = 0
        visited = set()
        while q and n-cnt > 2:
            # print(q)
            for _ in range(len(q)):
                cnt += 1
                node = q.popleft()
                visited.add(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if neigh not in visited and indegree[neigh] == 1:
                        q.append(neigh)
        res = []
        for i in range(n):
            if i not in visited:
                res.append(i)
        return q
        