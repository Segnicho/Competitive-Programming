class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(set)
        
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour, visited)
                    if found:
                        return True                        
            return False
        return dfs(source, set())
    