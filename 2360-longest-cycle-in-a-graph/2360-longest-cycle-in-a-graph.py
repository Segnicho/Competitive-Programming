class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        n = len(edges)
        indegree = [0]*n
        visited = set()
        for i, num in enumerate(edges):
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
                    if indegree[node] ==0:
                        nextL.append(node)
            q = nextL        
        seen = set()

        def dfs(i, start):
            nonlocal cycle
            if i in seen and i == start:
                cycle = True
                return
            if i in seen:
                return
            seen.add(i)
            for neigh in graph[i]:
                dfs(neigh, start)
        mx = -1
        for i in range(n):
            if i not in visited:
                seen = set()
                cycle = False
                dfs(i, i)
                if cycle:
                    visited |= seen
                    mx = max(mx, len(seen))
            visited.add(i)
        return mx
                    