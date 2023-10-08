# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(node):
            if not node:
                return None
            if node is p or node is q:
                return node
            left = recur(node.left)
            right = recur(node.right)
            if left and right:
                return node
            else:
                return left or right
        return recur(root)