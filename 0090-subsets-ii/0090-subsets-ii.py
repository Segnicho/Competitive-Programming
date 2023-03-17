class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(i, curr):
            res.append(curr[:])
            if i >= len(nums):
                return
            visited = set()
            for j in range(i, len(nums)):
                if nums[j] not in visited:
                    visited.add(nums[j])
                    curr.append(nums[j])
                    bt(j+1, curr)
                    curr.pop()
        nums.sort()
        bt(0, [])
        return res