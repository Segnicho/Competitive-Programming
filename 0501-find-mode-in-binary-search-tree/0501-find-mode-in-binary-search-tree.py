# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.count = Counter({})
        
        def FM(root):
            if not root:
                return 0
            self.count[root.val] += 1
            FM(root.left)
            FM(root.right)
        FM(root)
        res = []
        ls = list(sorted(self.count.items(), key=lambda item: item[1], reverse = True))
        mx = max(self.count.values())
        for i in range(len(ls)):
            if ls[i][1] == mx:
                res.append(ls[i][0])
            else:
                break
        return res
        