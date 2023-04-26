# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        def bfs(node):
            queue = deque([node])            
            
            while queue:
                sm = 0
                cnt = 0
                n = len(queue)
                for _ in range(len(queue)):
                    node = queue.popleft()
                    sm += node.val
                    cnt += 1
                    if node.left:
                        neighbour = node.left
                        queue.append(neighbour)
                    if node.right:
                        neighbour = node.right
                        queue.append(neighbour)
                res.append(sm/cnt)
        bfs(root)
        return res