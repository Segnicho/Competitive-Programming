# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        if not root:
            return False
        q = [[root, 0, 0]]
        res = Counter()
        while q:
            node, parent, level = q.pop()
            res[node.val] = [parent, level]
            if node.left:
                q.append([node.left, node.val, level+1])
            if node.right:
                q.append([node.right, node.val, level+1])
        if res[x][1] == res[y][1] and res[x][0] != res[y][0]:
            return True
        return False