class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        q = deque()
        
        for a, b in prerequisites:
            indegree[b] += 1
            graph[a].append(b)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        parents = defaultdict(set)
        dikt = {}
        i = 0
        while q:
            i += 1
            for _ in range(len(q)):
                node = q.popleft()
                dikt[node] = i
                for neigh in graph[node]:
                    parents[neigh].add(node)
                    indegree[neigh] -= 1
                    parents[neigh] |= parents[node]
                    if indegree[neigh] == 0:
                        q.append(neigh)
        ans = []
        for pre, post in queries:
            if dikt[pre] < dikt[post] and pre in parents[post]:
                ans.append(True)
            else:
                ans.append(False)
        return ans