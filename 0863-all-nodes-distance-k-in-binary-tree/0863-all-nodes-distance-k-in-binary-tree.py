# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def buildGraph(node, child):
            if node and child:
                graph[node.val].append(child.val)
                graph[child.val].append(node.val)
            if child.left:
                buildGraph(child, child.left)
            if child.right:
                buildGraph(child, child.right) 
        buildGraph(None, root)
        
        visited = set()
        def bfs(node):
            q = [node]
            visited.add(node)
            for _ in range(k):
                nxt = []
                for node in q:
                    for neigh in graph[node]:
                        if neigh not in visited:
                            nxt.append(neigh)
                            visited.add(neigh)
                q = nxt
            return q
        return bfs(target.val)
        
                    
        