# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0, 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            lcount, rcount = left[1] , right[1]
            lsum, rsum = left[0], right[0]
            
            if (lsum + rsum + node.val)//(lcount+rcount+1) == node.val:
                self.res += 1
                
            return node.val + lsum + rsum , 1 + lcount + rcount
        dfs(root)
        return self.res