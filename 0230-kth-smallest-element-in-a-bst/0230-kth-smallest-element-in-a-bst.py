# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def bst(root, arr):
            if not root:
                return
            bst(root.left, arr)
            arr.append(root.val)
            bst(root.right, arr)
        arr = []
        bst(root, arr)
        return arr[k-1]