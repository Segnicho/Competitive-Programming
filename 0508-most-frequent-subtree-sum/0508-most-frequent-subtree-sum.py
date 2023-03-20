# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(root = root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)            
            self.res.append(root.val + left + right)
            return self.res[-1]
        dfs()
        count = Counter(self.res)
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        ans = []
        mx = max(count.values())
        for val in count:
            if count[val] == mx:
                ans.append(val)
            else:
                break
        return ans