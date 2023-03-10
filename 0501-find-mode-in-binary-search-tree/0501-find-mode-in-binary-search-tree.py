# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = Counter({})
        def FM(root):
            if not root:
                return 0
            count[root.val] += 1
            FM(root.left)
            FM(root.right)
        FM(root)
        res = []
        mx = max(count.values())
        for ky, val in (count.items()):
            if count[ky] == mx:
                res.append(ky)
        return res
        