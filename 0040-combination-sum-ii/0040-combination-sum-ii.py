class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = []
        def rec(i=0, temp=[], sm=0):
            if i == n:
                if sm == target:
                    res.append(temp[:])
                return
            if sm > target:
                return
            temp.append(nums[i])
            visited.append(nums[i])
            sm += nums[i]
            rec(i+1, temp, sm)
            visited.pop()
            sm -= temp.pop()
            if nums[i] not in visited:
                rec(i+1, temp, sm)
        nums.sort()
        rec()
        return res