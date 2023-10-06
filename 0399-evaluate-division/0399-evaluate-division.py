class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        
        for i, (divisor, dividend )in enumerate(equations):
            graph[divisor].append([dividend, values[i]])
            graph[dividend].append([divisor, 1/values[i]])
        
        res = []
        
        def solve(start, end):
            if start not in graph or end not in graph:
                return -1
            q = deque([[start, 1]])
            visited =set()
            while q:
                node, curr = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == end:
                    return curr
                for neigh, weigh in graph[node]:
                    q.append([neigh, weigh*curr])
            return -1
        
        for dvs, dvdn in queries:
            ans = solve(dvs, dvdn)
            res.append(ans)
        return res
        