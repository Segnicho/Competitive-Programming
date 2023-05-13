class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        print(q)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        if len(res) != numCourses:
            return 0
        return True