# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        prefSum = Counter({0:1})
        def dfs(root = root,currSum = 0):
            if not root:
                return 0
            currSum += root.val
            self.res += prefSum[currSum-targetSum]
            prefSum[currSum] += 1
            dfs(root.left, currSum )
            dfs(root.right, currSum )
            prefSum[currSum] -= 1
        dfs()
        return self.res