class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        n = len(edges)
        indegree = [0]*n
        visited = set()
        for i, num in enumerate(edges):
            if num != -1:
                graph[i].append(num)
                indegree[num] += 1
        q  = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            nextL = []
            for num in q:
                visited.add(num)
                for node in graph[num]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        nextL.append(node)
            q = nextL        
        seen = set()
        def dfs(node):
            if not node in seen and node not in visited:
                seen.add(node)
                visited.add(node)
                for neigh in graph[node]:
                    dfs(neigh)
        mx = -1
        for i in range(n):
            if i not in visited:
                seen = set()
                dfs(i)
                mx = max(mx, len(seen))
        return mx
                    