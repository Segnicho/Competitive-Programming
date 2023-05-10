from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		graph = defaultdict(set)
		cycle = 0
		for i, arr in enumerate(adj):
		    if arr:
		        graph[i] = arr
		 
		def dfs(i,  parent, start):
		    nonlocal cycle
		    if i in visited:
		        cycle = 1
		        return
		    visited.add(i)
		    for num in graph[i]:
		        if num != parent or num != i:
		            dfs(num, i, start)
		            
        for num in graph:
            
            dfs(num, "parent", num)
            if cycle:
                break
        return cycle

