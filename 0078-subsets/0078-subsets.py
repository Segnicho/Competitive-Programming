class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []
        def dfs(i):
            if i >= n:
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res