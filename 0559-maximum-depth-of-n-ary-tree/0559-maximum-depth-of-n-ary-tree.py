"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.mx = 0
        
        def dfs(node,visited, depth):
            if not node:
                return 0
            
            depth += 1
            self.mx = max(self.mx, depth)
            visited.add(node)
            for child in node.children:
                if child not in visited:
                    dfs(child, visited, depth)
        dfs(root, set(), 0)
        
        return self.mx