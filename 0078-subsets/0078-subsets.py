class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i , temp):
            res.append(temp[:])
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                temp.append(nums[j])
                dfs(j+1, temp)
                temp.pop()
            
        dfs(0, [])
        
        return res
        