# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(node = root):
            
            q = deque([node])
            while q:
                curr = []
                for _ in range(len(q)):
                    node = q.popleft()
                    curr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(curr)
        if not root: return res        
        bfs()
        return res