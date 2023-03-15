# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # node= TreeNode(max(nums))
        def rec(nums = nums):
            if not nums:
                return
            if len(nums) == 1:
                return TreeNode(nums[0])
            mx = max(nums)
            ind = nums.index(mx)
            node = TreeNode(val = mx)
            node.left = rec(nums[:ind])
            node.right = rec(nums[ind+1:])
            return node
        return rec()