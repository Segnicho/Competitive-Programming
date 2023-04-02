class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        sm = nums[0]
        lg = nums[-1]
        def computeGCD(lg, sm):
            if  sm == 0:
                return lg
            return computeGCD(sm, lg%sm)
        return computeGCD(lg, sm)