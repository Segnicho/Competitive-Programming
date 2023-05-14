class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        i = 0
        dikt = Counter()
        parents = defaultdict(set)
        while q:
            i += 1
            for _ in range(len(q)):
                node = q.popleft()
                dikt[node] = i
                res.append(node)
                for neigh in graph[node]:
                    parents[neigh].add(node)
                    parents[neigh] |= parents[node]
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        q.append(neigh)
        ans = []
        for pre, post in queries:
            if dikt[pre] < dikt[post] and pre in parents[post]:
                ans.append(True)
            else:
                ans.append(False)
        return ans