# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        dummy = root
        
        node = TreeNode(val)
        if not root:
            return node
        else:
            def insertToBST(root, val):
                if val < root.val:
                    if not root.left:
                        root.left = node
                        return None
                    return insertToBST(root.left, val)
                else:
                    if not root.right:
                        root.right = node
                        return  None
                    return insertToBST(root.right, val)
            insertToBST(dummy, val)
            return root

        