# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = root
        def dNode(root, key):
            if not root: 
                return root
            elif key < root.val:
                root.left = dNode(root.left, key)
            elif key > root.val:
                root.right = dNode(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    successor = root.right
                    while successor.left:
                        successor = successor.left
                    root.val = successor.val
                    root.right = dNode(root.right, successor.val)
            return root
        return dNode(root, key)