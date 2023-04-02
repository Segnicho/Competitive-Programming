class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        def GCD(a, b):
            if not b:
                return a
            return GCD(b, a%b)
        for i in range(len(nums) ):
            gcd = 0
            for j in range(i, len(nums)):
                gcd = GCD(gcd, GCD(nums[i], nums[j]))
                if gcd == k:
                    res += 1
        return res
    