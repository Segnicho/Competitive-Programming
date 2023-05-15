from collections import defaultdict, deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    indegree = [0]*n
    graph = defaultdict(list)
    for u, v in prerequisites:
        graph[u-1].append(v-1)
        indegree[v-1] += 1
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    res = []
    ans = []
    while q:
        curr = []
        for _ in range(len(q)):
            node = q.popleft()
            res.append(node)
            curr.append(node)

            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        ans.append(curr)
    if len(res) != n:
        return -1
    return len(ans)
