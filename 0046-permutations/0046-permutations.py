class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if n == 1:
            return [nums[:]]
        for i in range(n):
            num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(num)
                res.append(perm)
            nums.append(num)
            
        return res