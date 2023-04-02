class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums) ):
            GCD = 0
            for j in range(i, len(nums)):
                GCD = gcd(GCD, gcd(nums[i], nums[j]))
                if GCD == k:
                    res += 1
                elif GCD < k:
                    break
        return res
    