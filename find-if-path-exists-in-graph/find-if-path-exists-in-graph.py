class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        q = deque([source])
        visited = set()
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neigh in graph[node]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
        return False