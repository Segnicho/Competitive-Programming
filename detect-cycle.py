from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		graph = defaultdict()
		cycle = 0
		visited = set()
		for i, arr in enumerate(adj):
		    if arr:
		        graph[i] = arr
		def dfs(node,  parent):
		    nonlocal cycle
		    visited.add(node)
		    for neigh in graph[node]:
		        if neigh not in visited:
		            if dfs(neigh, node):
		                return True
		        elif neigh != parent:
		            cycle = True
		            return cycle
        for num in graph:
            if num not in visited:
                dfs(num, -1)
                if cycle:
                    return 1
        return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
