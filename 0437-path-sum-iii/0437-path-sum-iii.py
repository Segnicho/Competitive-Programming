# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        counter = Counter({0:1})
        def dp(root = root,sm = 0):
            if not root:
                return 0
            sm += root.val
            self.res += counter[sm-targetSum]
            counter[sm] += 1
            dp(root.left, sm )
            dp(root.right, sm )
            counter[sm] -= 1
        dp()
        return self.res
    