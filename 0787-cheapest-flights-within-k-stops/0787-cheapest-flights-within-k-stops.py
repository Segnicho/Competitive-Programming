class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        distances = defaultdict()
        
        for source, dest, weight in flights:
            distances[source] = math.inf
            distances[dest] = math.inf
            graph[source].append([dest, weight])
        q = [[0, src, -1]]
        distances[src] = 0
        visited = defaultdict(int)
        while q:
            weight, node, distance = heappop(q)
            if node == dst and distance <= k:
                return weight
            if visited[node] > 10:
                continue
            visited[node] += 1
            for neigh, weigh in graph[node]:
                dist = weigh+weight
                # if dist < distances[neigh]:
                distances[neigh] = dist
                heappush(q, [dist, neigh , distance+ 1])
        return -1
            