class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums) ):
            LCM = nums[i]
            for j in range(i, len(nums)):
                LCM = lcm(LCM, lcm(nums[i], nums[j]))
                if LCM == k:
                    res += 1
                if LCM > k:
                    break
        return res