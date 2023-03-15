# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # preorder.sort()
        def rec(nums):
            
            if not nums:
                return None
            root = TreeNode(nums[0])
            i = 1
            t = False
            
            while i < len(nums):
                if nums[i] > nums[0]:
                    t =True
                    break
                i += 1
            if t:
                root.left = rec(nums[1:i])
                root.right = rec(nums[i:])
            else:
                root.right = rec(nums[i:])
                root.left = rec(nums[1:i])
            return root
        
        return rec(preorder)
