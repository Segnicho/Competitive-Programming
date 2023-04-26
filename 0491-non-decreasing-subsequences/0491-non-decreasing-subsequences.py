class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        vis = {}
        def dfs(i):
            # global res
            if len(res) >= 2:
                vis[tuple(res)] = 1
            for j in range(i, len(nums)):
                if not res or (nums[j] >= res[-1]):
                    res.append(nums[j])
                    dfs(j+1)
                    res.pop()
                    
        dfs(0) 
        return vis.keys()
    