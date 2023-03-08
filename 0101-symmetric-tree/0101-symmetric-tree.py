# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return True
        def isSy(lNode, rNode):
            if lNode and rNode:
                return lNode.val == rNode.val and isSy(lNode.right, rNode.left) and                                     isSy(lNode.left, rNode.right)
            return lNode == rNode
        return isSy(root.left, root.right)