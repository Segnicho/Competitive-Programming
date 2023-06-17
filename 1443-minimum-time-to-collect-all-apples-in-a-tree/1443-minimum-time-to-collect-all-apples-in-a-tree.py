class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        def dfs(node, parent):
            time = 0
            for child in graph[node]:
                if child != parent:
                    time += dfs(child, node)
            if (hasApple[node] or time > 0) and node != 0:
                return time + 2
            return time
        return dfs(0, -1)
    