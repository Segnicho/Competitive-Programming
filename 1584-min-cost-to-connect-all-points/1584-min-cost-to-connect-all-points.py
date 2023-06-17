class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                graph[i].append([dist, j])
                graph[j].append([dist, i])
        
        mnHeap = [[0, 0]]
        visited = set()
        cost = 0
        while mnHeap:
            dist, node = heappop(mnHeap)
            if node not in visited:
                visited.add(node)
                cost += dist
                for neighCost, neigh in graph[node]:
                    if neigh not in visited:
                        heappush(mnHeap, [neighCost, neigh])
        return cost