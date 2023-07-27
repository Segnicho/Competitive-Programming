class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        visited = set()
        def backtrack():
            
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack()
                    path.pop()
                    visited.remove(nums[i])
        backtrack()
        return res
    