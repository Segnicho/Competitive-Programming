class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i=0, sm=0, temp =  []):
            
            if sm == target:
                res.append(temp[:])
                return
            if sm > target:
                return
            for j in range(i, len(nums)):
                sm += nums[j]
                temp.append(nums[j])
                dfs(j, sm, temp)
                sm -= temp[-1]
                temp.pop()
        dfs()
        return res